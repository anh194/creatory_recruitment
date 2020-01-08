# -*- coding: utf-8 -*-

import datetime
from ..factory import db

class VideoMeasurement(db.Model):
	__tablename__ = 'video_measurement'

	id = db.Column(db.Integer(), primary_key=True)
	video_id = db.Column(db.String(128), db.ForeignKey('video.id', ondelete="CASCADE"))
	video = db.relationship("Video", back_populates="measurements")
	measurement_date = db.Column(db.DateTime())
	comments = db.Column(db.Integer(), server_default=db.text("0"))
	views = db.Column(db.Integer(), server_default=db.text("0"))
	likes = db.Column(db.Integer(), server_default=db.text("0"))
	dislikes = db.Column(db.Integer(), server_default=db.text("0"))


class Video(db.Model):
	__tablename__ = 'video'

	id = db.Column(db.Integer(), primary_key=True)
	youtube_id = db.Column(db.String(128))
	channel_id = db.Column(db.String(128), db.ForeignKey('channel.id'))
	channel = db.relationship("Channel", back_populates="videos")
	create_date = db.Column(db.DateTime())
	title = db.Column(db.String(128))
	description = db.Column(db.Text())
	duration = db.Column(db.Integer())
	measurements = db.relationship(
        "VideoMeasurement", cascade="all,delete",
        back_populates="video", passive_deletes=True)


class Channel(db.Model):
	__tablename__ = 'channel'

	id = db.Column(db.Integer(), primary_key=True)
	channel_id = db.Column(db.String(128))
	name = db.Column(db.String(128))
	subscribe = db.Column(db.Integer())
	videos = db.relationship("Video")












