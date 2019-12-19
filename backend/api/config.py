"""
    config.py
    - settings for the flask application object
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app_v1.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # used for encryption and session management
    SECRET_KEY = 'asdlkjhfESDFJja023r;a==fkaslrj2ori2r1sdvBKEW'
    FLASKY_ADMIN = 'Administrator@papayaer.me'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_POSTS_PER_PAGE = 6 #文章页每页的数量
    FLASKY_FOLLOWERS_PER_PAGE = 10 #粉丝页每页的数量
    FLASKY_COMMENTS_PER_PAGE = 10 #评论每页的数量
    FLASKY_SLOW_DB_QUERY_TIME = 0.5