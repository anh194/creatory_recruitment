# -*- coding: utf-8 -*-
"""
	admin.factory
	~~~~~~~~~~~~~

	admin factory module
"""

import os

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import locale

from .helpers import register_blueprints
from .config import config


# Suppress InsecureRequestWarning
import urllib3
urllib3.disable_warnings()

db = SQLAlchemy()

def create_app(package_name, package_path, settings_override=None, register_security_blueprint=True):
	"""Returns a :class:`Flask` application instance configured with common
	functionality for the CBP Admin platform.

	:param package_name: application package name
	:param package_path: application package path
	:param settings_override: a dictionary of settings to override
	:param register_security_blueprint: flag to specify if the Flask-Security
										Blueprint should be registered. Defaults to `True`.
	"""
	app = Flask(package_name, instance_relative_config=True)

	config_name = os.getenv('FLASK_CONFIG') or 'default'
	app.config.from_object(config[config_name])
	app.config.from_pyfile('settings.cfg', silent=True)
	app.config.from_object(settings_override)
	
	app.app_context().push()
	CORS(app)
	db.init_app(app)
	register_blueprints(app, package_name, package_path)

	with app.app_context():
		db.create_all()

	return app
