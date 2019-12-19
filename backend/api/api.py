"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""
from flask import Blueprint

api = Blueprint('api', __name__)

# @api.route('/hello/<string:name>/')
# def say_hello(name):
#     response = { 'msg': "Hello {}".format(name) }
#     return jsonify(response)


from . import authentication, roles, users, posts, comments, follows, favorites, notifications, messages, tasks, errors 
