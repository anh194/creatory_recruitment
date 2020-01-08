# -*- coding: utf-8 -*-

import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	LOCALE = 'en_GB.utf8'
	CACHE_TIMEOUT = 60 * 60
	JSONIFY_PRETTYPRINT_REGULAR = False
	APP_VERSION = '0.0.1'
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'database.db')
	JSONIFY_PRETTYPRINT_REGULAR = True



class ProductionConfig(Config):
	pass


config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,

	'default': DevelopmentConfig
}

GOOGLE_API_KEY = 'AIzaSyBrZNoukoVxp7H-KWo29bYZnyx7RekcDEU'