from flask import current_app, jsonify, request, url_for
from .api import api
from models import db, Permission, User, Follow

from .authentication import permission_required

# 检查是否已关注
@api.route('/users/<int:id>/following/', methods=['GET'])
@permission_required(Permission.FOLLOW)
def has_follow(user, id):
    followed = User.query.get_or_404(id)
    follower = user.is_following(followed)
    return jsonify(follower)


# 加关注
@api.route('/users/<int:id>/follow/', methods=['POST'])
@permission_required(Permission.FOLLOW)
def new_follow(user, id):
    followed = User.query.get_or_404(id)
    user.follow(followed)
    db.session.commit()
    return jsonify(followed.id)


# 取消关注
@api.route('/users/<int:id>/unfollow/', methods=['POST'])
@permission_required(Permission.FOLLOW)
def un_follow(user, id):
    followed = User.query.get_or_404(id)
    user.unfollow(followed)
    db.session.commit()
    return jsonify(followed.id)