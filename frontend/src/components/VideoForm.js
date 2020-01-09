import React, {useState} from 'react';
import { Form, Input, Button } from 'semantic-ui-react'

export const VideoForm = ({onNewVideo}) => {
	const [videoId, setVideoId] = useState('')
	// const [videos, setVideos] = useState()

	return(
		<Form>
			<Form.Field>
				<Input placeholder="Video ID" 
				value={videoId} 
				onChange={e => setVideoId(e.target.value)}/>
			</Form.Field>
			<Form.Field>
				<Button onClick={async() => {
					var link = '/video?video_id=' + videoId
					var result
					const response = await fetch(link).then(
						response => response.json().then(
							data => {
								result = data
							}
						)
					)

					console.log("Work");
					onNewVideo(result)
				}}>
					Search
				</Button>
			</Form.Field>
		</Form>
	)
}