from ..config import GOOGLE_API_KEY
from ..factory import db
from ..database.models import Video
from flask import Blueprint, current_app as app, abort, jsonify, request

from googleapiclient.discovery import build

import isodate
import datetime
import dateutil.parser

bp = Blueprint('video', __name__)
@app.route('/video', methods=['GET'])
def search_video():
	arg = request.args

	if 'video_id' not in arg:
		return {"error": "please provide video id"}

	api_service_name = "youtube"
	api_version = "v3"

	youtube = build(api_service_name, api_version, developerKey=GOOGLE_API_KEY)
	result = youtube.videos().list(
		part = "snippet,contentDetails",
		id = arg['video_id']
	)

	response = result.execute()
	if not response['items']:
		return {"error": "no video match this id"}

	duration = response['items'][0]['contentDetails']['duration']
	dur = isodate.parse_duration(duration)
	duration =dur.total_seconds()


	description = response['items'][0]['snippet']['description']

	title = response['items'][0]['snippet']['title']

	date = response['items'][0]['snippet']['publishedAt']

	youtube_id = response['items'][0]['id']

	channel_id = response['items'][0]['snippet']['channelId']

	format_response = {'youtube_id': youtube_id,
					'channel_id': channel_id,
					'date': date,
					'title': title,
					'description': description,
					'duration': duration}

	insert_video_to_db(format_response)
	return format_response


def insert_video_to_db(data):

	if not data:
		print('Error. Can not copy record to DB.')
		return

	# make sure every video in DB is unique.
	exist = db.session.query(Video).filter_by(youtube_id=data['youtube_id']).first() is not None
	if exist:
		return
		
	date = dateutil.parser.parse(data['date'])
	youtube_id = data['youtube_id']
	channel_id = data['channel_id']
	title = data['title']
	description = data['description']
	duration = data['duration']

	video = Video(youtube_id=youtube_id, channel_id=channel_id, create_date=date,
				title=title, description=description, duration=duration)

	db.session.add(video)
	db.session.commit()

