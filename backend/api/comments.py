from flask import current_app, jsonify, request, url_for
from .api import api
from models import db, Permission, User, Post, Comment

from .authentication import permission_required
from .errors import forbidden

import json


# 当前文章的所有评论
@api.route('/posts/<int:id>/comments/', methods=['GET'])
def get_post_comments(id):
    post = Post.query.get_or_404(id)
    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.timestamp.desc())
    page = request.args.get('page', 1, type=int)
    pagination = comments.paginate(page,
        per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_post_comments', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_post_comments', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })
    # return jsonify([comment.to_json() for comment in comments])


# 写当前文章的评论
@api.route('/posts/<int:id>/comments/', methods=['POST'])
@permission_required(Permission.COMMENT)
def new_comment(user, id):
    jsonStr = json.loads(request.get_data(as_text=True))
    post = Post.query.get_or_404(id)
    comment = Comment.from_json(jsonStr)
    comment.post_id = post.id
    comment.author_id = user.id
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_json()), 201