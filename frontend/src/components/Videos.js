import React from 'react';
import { Container, Header } from "semantic-ui-react";

export const Videos = ({ videos }) => {
	if (videos){
		return (
		<Container text>
			<Header style={ { marginTop: 40} }>{videos.title}</Header>
			<p> <b>Date</b>: {videos.date}</p>
			<p> <b>Duration</b>: {videos.duration}</p>
			<p> <b>Channel ID</b>:{videos.channel_id}</p>
			<p> <b>Youtube ID</b>: {videos.youtube_id}</p>
			<p> <b>Description</b>: {videos.description}</p>
		</Container>
		)
	}else{
		return(
			<p></p>
		)
	}
}