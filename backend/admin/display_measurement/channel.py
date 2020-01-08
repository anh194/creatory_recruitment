from ..config import GOOGLE_API_KEY
from ..factory import db
from ..database.models import Channel
from flask import Blueprint, current_app as app, abort, jsonify, request

from googleapiclient.discovery import build

import isodate
import datetime
import dateutil.parser

bp = Blueprint('channel', __name__)
@app.route('/channel', methods=['GET'])
def search_channel():
	arg = request.args

	if 'channel_id' not in arg:
		return {"error": "please provide channel id"}

	api_service_name = "youtube"
	api_version = "v3"

	youtube = build(api_service_name, api_version, developerKey=GOOGLE_API_KEY)
	result = youtube.channels().list(
		part = "statistics, snippet",
		id = arg['channel_id']
	)

	response = result.execute()

	if not response['items']:
		return {"error": "no channel match this id"}

	name = response['items'][0]['snippet']['title']
	subscribe = response['items'][0]['statistics']['subscriberCount']
	channel_id = response['items'][0]['id']

	format_response = {'name': name, 'subscribe': subscribe, 'channel_id': channel_id}

	insert_channel_to_db(format_response)

	return format_response

def insert_channel_to_db(data):
	if not data:
		print('Error. Can not copy record to DB.')
		return

	exist = db.session.query(Channel).filter_by(channel_id=data['channel_id']).first() is not None

	if exist:
		return

	name = data['name']
	subscribe = data['subscribe']
	channel_id = data['channel_id']

	channel = Channel(name=name, subscribe=subscribe, channel_id=channel_id)

	db.session.add(channel)
	db.session.commit()
