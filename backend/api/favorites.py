from flask import current_app, jsonify, request, url_for
from .api import api
from models import db, Permission, User, Post, Favorite

from .authentication import permission_required

# 收藏了吗?
@api.route('/posts/<int:id>/favoriting/', methods=['GET'])
@permission_required(Permission.FOLLOW)
def has_favorit(user, id):
    post = Post.query.get_or_404(id)
    isfavorite = user.is_favoriting(post)
    return jsonify(isfavorite)


# 加收藏
@api.route('/posts/<int:id>/favorite/', methods=['POST'])
@permission_required(Permission.WRITE)
def new_favorite(user, id):
    post = Post.query.get_or_404(id)
    user.do_favorite(post)
    db.session.commit()
    return jsonify(post.id)


# 取消收藏
@api.route('/posts/<int:id>/unfavorite/', methods=['POST'])
@permission_required(Permission.WRITE)
def un_favorite(user, id):
    post = Post.query.get_or_404(id)
    user.unfavorite(post)
    db.session.commit()
    return jsonify(post.id)