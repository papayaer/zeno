from flask import current_app, jsonify, request, url_for
from .api import api
from models import Permission, Post, User, Follow, Favorite, Comment

from .authentication import permission_required



# 当前用户的信息
@api.route('/users/<int:id>/', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


# 我的文章列表
@api.route('/users/<int:id>/posts/', methods=['GET'])
def get_user_posts(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_posts', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_posts', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


# 我关注的人的文章和我自己的文章,(不包括收藏的文章)
@api.route('/users/<int:id>/followed/posts/', methods=['GET'])
def get_followed_post(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.followed_user_posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_followed_post', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_followed_post', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


# 我的关注
@api.route('/users/<int:id>/followed/', methods=['GET'])
def get_user_followed(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.followed_users.order_by(Follow.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_followed', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_followed', id=id, page=page+1)
    return jsonify({
        'follower': user.nickname,
        'followed': [post.to_json_followed() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


# 我的粉丝
@api.route('/users/<int:id>/followers/', methods=['GET'])
def get_user_followers(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.follower_users.order_by(Follow.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_followers', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_followers', id=id, page=page+1)
    return jsonify({
        'followed': user.nickname,
        'followers': [post.to_json_follower() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


# 我收藏的文章
@api.route('/users/<int:id>/favorite/', methods=['GET'])
# @permission_required(Permission.FOLLOW)
def get_user_favorite_posts(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.favorite.order_by(Favorite.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_favorite_posts', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_favorite_posts', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


# author参与的讨论
@api.route('/users/<int:id>/comments/', methods=['GET'])
def get_user_comments(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.get_user_comment.order_by(Comment.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_comments', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_comments', id=id, page=page+1)
    return jsonify({
        'user': user.nickname,
        'comments': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

