from ..config import GOOGLE_API_KEY
from ..factory import db
from ..database.models import VideoMeasurement
from flask import Blueprint, current_app as app, abort, jsonify, request

from googleapiclient.discovery import build

import isodate
import datetime
import dateutil.parser

bp = Blueprint('measurement', __name__)
@app.route('/measurement', methods=['GET'])
def search_measurement():
	arg = request.args

	if 'video_id' not in arg:
		return {"error": "please provide video id"}

	api_service_name = "youtube"
	api_version = "v3"

	youtube = build(api_service_name, api_version, developerKey=GOOGLE_API_KEY)
	result = youtube.videos().list(
		part = "statistics",
		id = arg['video_id']
	)

	response = result.execute()

	if not response['items']:
		return {"error": "no video match this id"}

	video_id = response['items'][0]['id']
	comment = response['items'][0]['statistics']['commentCount']
	dislike = response['items'][0]['statistics']['dislikeCount']
	like = response['items'][0]['statistics']['likeCount']
	view = response['items'][0]['statistics']['viewCount']
	now = datetime.datetime.now()
	now = now.strftime("%Y-%m-%d %H:%M:%S.%f")

	format_response = {'video_id': video_id,
					'comment': comment,
					'dislike': dislike,
					'like': like,
					'view': view,
					'time': now}

	insert_measurement_to_db(format_response)

	return format_response

def insert_measurement_to_db(data):
	if not data:
		print('Error. Can not copy record to DB.')
		return

	video_id = data['video_id']
	comment = data['comment']
	dislike = data['dislike']
	like = data['like']
	view = data['view']
	time = dateutil.parser.parse(data['time'])

	measurement = VideoMeasurement(video_id=video_id, measurement_date=time, comments=comment,
				dislikes=dislike, likes=like, views=view)

	db.session.add(measurement)
	db.session.commit()
