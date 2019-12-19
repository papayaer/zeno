from flask import request, jsonify, current_app
from datetime import datetime, timedelta
from functools import wraps
from .errors import forbidden
import jwt
import json

from models import db, User, Permission

from .api import api

def permission_required(permission):
    def token_required(f):
        @wraps(f)
        def _verify(*args, **kwargs):
            auth_headers = request.headers.get('Authorization', '').split()

            invalid_msg = {
                'status': '401',
                'message': 'Invalid token. Registeration and / or authentication required',
                'authenticated': False
            }
            expired_msg = {
                'status': '401',
                'message': 'Expired token. Reauthentication required.',
                'authenticated': False
            }

            if len(auth_headers) != 1:
                return jsonify(invalid_msg), 401
                # return jsonify(auth_headers)
            # token = auth_headers[0]
            # data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm=['HS256'])
            # user = User.query.filter_by(email=data['sub']).first()
            # return jsonify({'data': user.can(permission)})

            try:
                token = auth_headers[0]
                data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm=['HS256'])
                user = User.query.filter_by(email=data['sub']).first()
                if not user:
                    raise RuntimeError('User not found')
                if not user.can(permission):
                    return forbidden('Insufficient permissions')
                return f(user, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
            except (jwt.InvalidTokenError, Exception) as e:
                print(e)
                return jsonify(invalid_msg), 401

        return _verify
    return token_required


@api.route('/register/', methods=['POST'])
def register():
    # data = request.json
    data = json.loads(request.get_data(as_text=True))
    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({'msg': 'user had'}), 401
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201


@api.route('/login/', methods=['POST'])
def login():
    # data = request.json
    data = json.loads(request.get_data(as_text=True))
    user = User.authenticate(**data)

    if not user:
        return jsonify({ 'status': '401', 'message': 'Invalid credentials', 'authenticated': False }), 401

    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({ 
        'token': token.decode('UTF-8'),
        'user': user.to_dict(include_email=True)
        })


@api.route('/users/<int:id>/', methods=['PUT'])
@permission_required(Permission.WRITE)
def update_user(user,id):
    if user.id != id:
        return jsonify({'msg': 'user is null'}), 401
    user = User.query.get_or_404(id)
    data = json.loads(request.get_data(as_text=True))
    user.from_dict(data, password=False)
    db.session.commit()
    return jsonify(user.to_json()), 201


# 前端重新获取用户信息
@api.route('/users/<int:id>/ref/', methods=['GET'])
@permission_required(Permission.WRITE)
def ref_user(user,id):
    if user.id != id:
        return jsonify({'msg': 'user is null'}), 401
    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({ 
        'token': token.decode('UTF-8'),
        'user': user.to_dict(include_email=True)
        })
