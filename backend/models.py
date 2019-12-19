"""
models.py
- Data classes for the papayaerapi application
"""

from datetime import datetime
from markdown import markdown
import bleach
from exceptions import ValidationError

from flask import current_app, request, url_for
# import hashlib
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            'Moderator': [Permission.FOLLOW, Permission.COMMENT,
                          Permission.WRITE, Permission.MODERATE],
            'Administrator': [Permission.FOLLOW, Permission.COMMENT,
                              Permission.WRITE, Permission.MODERATE,
                              Permission.ADMIN],
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return '<Role %r>' % self.name


class Follow(db.Model):
    __tablename__ = 'follows'

    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


    def to_json_follower(self):
        json_post = {
            # 'id': self.followed.id,
            # 'username': self.followed.username,
            # 'nickname': self.followed.nickname,
            'timestamp': self.timestamp,
            'user': self.follower.to_dict()
        }
        return json_post
    
    def to_json_followed(self):
        json_post = {
            # 'id': self.follower.id,
            # 'username': self.follower.username,
            # 'nickname': self.follower.nickname,
            'timestamp': self.timestamp,
            'user': self.followed.to_dict()
        }
        return json_post


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    nickname = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    website_url = db.Column(db.Text)
    bio = db.Column(db.Text)
    profile_pic = db.Column(db.Text)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    last_message_read_time = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(32))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    favorite = db.relationship('Favorite', backref='author', lazy='dynamic')
    followed = db.relationship('Follow',
                               foreign_keys=[Follow.follower_id],
                               backref=db.backref('follower', lazy='joined'),
                               lazy='dynamic',
                               cascade='all, delete-orphan')
    followers = db.relationship('Follow',
                                foreign_keys=[Follow.followed_id],
                                backref=db.backref('followed', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic')
    tasks = db.relationship('Task', backref='user', lazy='dynamic')

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        # pw = generate_password_hash(password)
        # return pw
        
        if not email or not password:
            return None
        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return None

        return user

    def to_json(self):
        return dict(id=self.id, email=self.email)
    
    @staticmethod
    def add_self_follows():
        for user in User.query.all():
            if not user.is_following(user):
                user.follow(user)
                db.session.add(user)
                db.session.commit()

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = self.gravatar_hash()
        # 自己关注自己
        # self.follow(self)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('reset'))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps(
            {'change_email': self.id, 'new_email': new_email}).decode('utf-8')

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def gravatar_hash(self):
        db.session.flush()#刷新后可以取到最新插入的ID
        return 'https://randomuser.me/portraits/women/{img}.jpg'.format(img=self.id)

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()
    
    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        n = Notification(name=name, payload_json=json.dumps(data), user=self)
        db.session.add(n)
        return n

    def do_favorite(self, post):
        if not self.is_favoriting(post):
            f = Favorite(author_id = self.id, post_id = post.id)
            db.session.add(f)

    def unfavorite(self, post):
        f = self.favorite.filter_by(post_id=post.id).first()
        if f:
            db.session.delete(f)

    def is_favoriting(self, post):
        if post.id is None:
            return False
        return self.favorite.filter_by(
            post_id=post.id).first() is not None


    # 添加关注
    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)

    # 取消关注
    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)

    def is_following(self, user):
        if user.id is None:
            return False
        return self.followed.filter_by(
            followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        if user.id is None:
            return False
        return self.followers.filter_by(
            follower_id=user.id).first() is not None
 
    # author的关注
    @property
    def followed_users(self):
        return self.followed.filter_by(follower_id = self.id)

    # author的粉丝
    @property
    def follower_users(self):
        return self.followers.filter_by(followed_id = self.id)

    @property
    def followed_user_posts(self):
        # 我关注author的文章
        followed_posts = Post.query.join(Follow, Follow.followed_id == Post.author_id)\
            .filter(Follow.follower_id == self.id)
        # 我自己的文章
        own_posts = Post.query.filter_by(author_id = self.id)
        # 将两个查询合并为一个查询并返回
        return followed_posts.union(own_posts)
    
    
    # author参与的讨论
    @property
    def get_user_comment(self):
        return Comment.query.join(Post, Post.id==Comment.post_id).filter(Comment.author_id==self.id)


    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'url': url_for('api.get_user', id=self.id),
            'username': self.username,
            'nickname': self.nickname,
            'name': self.name,
            'role': self.role.name,
            'member_since': self.member_since,
            'last_seen': self.last_seen,
            'about_me': self.about_me,
            'bio': self.bio,
            'location': self.location,
            'website_url': self.website_url,
            'avatar': self.avatar_hash,
            'index_count': self.followed_user_posts.count(), # 动态计数
            'post_count': self.posts.count(), # 文章计数
            'follower_count': self.followers.count(), # 粉丝计数
            'followed_count': self.followed.count(), # 关注计数
            'favorite_count': self.favorite.count(), # 收藏计数
            'comment_count': self.comments.count(), # 评论计数
            'history_count': 0, # 浏览历史计数
            'notifications_count': self.notifications.count(), # 消息计数
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'followers_url': url_for('api.get_user_followers',
                                          id=self.id),
                'followed_url': url_for('api.get_user_followed',
                                          id=self.id),
                'posts_url': url_for('api.get_user_posts', id=self.id),
                'favorite_posts_url': url_for('api.get_user_favorite_posts', id=self.id),
                'comments_url': url_for('api.get_user_comments', id=self.id)
            }
        }
        if include_email:
            data['email'] = self.email
        return data


    def from_dict(self, data, password=False):
        for field in ['nickname', 'email', 'about_me', 'bio', 'avatar_hash']:
            if field in data:
                setattr(self, field, data[field])
        if password and 'password' in data:
            self.password(data['password'])


    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return '<User %r>' % self.username


# class AnonymousUser(AnonymousUserMixin):
#     def can(self, permissions):
#         return False

#     def is_administrator(self):
#         return False

# login_manager.anonymous_user = AnonymousUser


# @login_manager.user_loader RestAPI可能不需要这个功能，需要查清
def load_user(user_id):
    return User.query.get(int(user_id))




class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225))
    abstract = db.Column(db.String(225)) # 文章摘要
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    body_img = db.Column(db.Text) # 封面图片
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    favorite = db.relationship('Favorite', backref='favorite', lazy='dynamic')
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'p', 'blockquote', 'code', 'br'
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'span', 'div',
                        'h1', 'h2', 'h3', 'h4', 'table', 'thead', 'tbody', 'th', 'tr', 'td',
                        'mark', 'sup', 'kbd', 'img', 'video', 'source', 'hr', 'flow']
        allowed_attrs = {'*': ['class'],
                        'a': ['href', 'rel'],
                        'img': ['src', 'alt'],
                        'video': ['controls', 'autoplay', 'width', 'height',
                        'loop', 'muted', 'poster', 'preload','src', 'alt'],
                        'source': ['src', 'type', 'alt']
                        }
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, attributes=allowed_attrs, strip=True))



    def to_json(self):
        json_post = {
            # 'url': url_for('api.get_post', id=self.id),
            'id': self.id,
            'title': self.title,
            'abstract': self.abstract,
            'body': self.body,
            'body_html': self.body_html,
            'body_img': self.body_img,
            'timestamp': self.timestamp,
            'favorite_count': self.favorite.count(),
            'comment_count': self.comments.count(),
            # 'comment_url': url_for('api.get_post_comments', id=self.id),
            'author': self.author.to_dict()
        }
        return json_post

    @staticmethod
    def from_json(json_post):
        title = json_post.get('title')
        if title is None or title == '':
            title = None
        body_img = json_post.get('img')
        body = json_post.get('body')
        if body is None or body == '':
            raise ValidationError('post does not have a body')
        if body_img is None or body_img == '':
            body_img = None
        abstract = json_post.get('abstract')
        if abstract is None or abstract == '':
            abstract = body[0:139]
        return Post(body=body, title=title, abstract=abstract, body_img=body_img)

db.event.listen(Post.body, 'set', Post.on_changed_body)


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    disabled = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'p', 'blockquote', 'code', 'br'
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'span', 'div',
                        'h1', 'h2', 'h3', 'h4', 'table', 'thead', 'tbody', 'th', 'tr', 'td',
                        'mark', 'sup', 'kbd', 'img', 'video', 'source', 'hr', 'flow']
        allowed_attrs = {'*': ['class'],
                        'a': ['href', 'rel'],
                        'img': ['src', 'alt'],
                        'video': ['controls', 'autoplay', 'width', 'height',
                        'loop', 'muted', 'poster', 'preload','src', 'alt'],
                        'source': ['src', 'type', 'alt']
                        }
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, attributes=allowed_attrs, strip=True))

    
    def to_json(self):
        json_comment = {
            'post_id': self.post.id,
            'post_title': self.post.title,
            'url': url_for('api.get_user_comments', id=self.author_id),
            'post_url': url_for('api.get_post', id=self.post_id),
            'comment_body': self.body_html,
            'timestamp': self.timestamp,
            'author': self.author.to_dict()
        }
        return json_comment

    @staticmethod
    def from_json(json_comment):
        body = json_comment.get('body')
        if body is None or body == '':
            raise ValidationError('comment does not have a body')
        return Comment(body=body)

db.event.listen(Comment.body, 'set', Comment.on_changed_body)


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)


class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.Float, index=True, default=datetime.utcnow)
    payload_json = db.Column(db.Text)

    def get_data(self):
        return json.loads(str(self.payload_json))

# 消息队(Redis Queue)列表
class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    complete = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get('progress', 0) if job is not None else 100


class Favorite(db.Model):  
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    
    def to_json(self):
        json_post = {
            'timestamp': self.favorite.timestamp,
            'post': self.favorite.to_json()
        }
        return json_post
