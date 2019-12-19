from flask import current_app, jsonify, request, url_for
from .api import api
from models import db, Permission, Post, Comment

from .authentication import permission_required
from .errors import forbidden

import json

# 所有文章列表
@api.route('/posts/', methods=['GET'])
# @permission_required(Permission.WRITE)
def get_posts():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts', page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

# 当前文章
@api.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({'post': post.to_json()})

# 写新文章
@api.route('/posts/', methods=['POST'])
@permission_required(Permission.WRITE)
def new_post(user):
    jsonStr = json.loads(request.get_data(as_text=True))
    post = Post.from_json(jsonStr)
    post.author_id = user.id
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201, \
        {'Location': url_for('api.get_post', id=post.id)}

# 修改当前文章
@api.route('/posts/<int:id>', methods=['PUT'])
@permission_required(Permission.WRITE)
def edit_post(user, id):
    # return jsonify({'user_id': user.id, 'post_id': id})
    post = Post.query.get_or_404(id)
    if user.id != post.author_id and \
            not user.can(Permission.ADMIN):
        return forbidden('Insufficient permissions')
    post.body = request.json.get('body', post.body)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())
