import React, {useState} from 'react';
import { Form, Input, Button } from 'semantic-ui-react'

export const VideoForm = ({onNewVideo}) => {
	const [videoId, setVideoId] = useState('')

	return(
		<Form>
			<Form.Field>
				<Input placeholder="Video ID. Example: wdH26D8Ssww" 
				value={videoId} 
				onChange={e => setVideoId(e.target.value)}/>
			</Form.Field>
			<Form.Field>
				<Button onClick={async() => {
					var link_video = '/video?video_id=' + videoId
					var link_measurement = '/measurement?video_id=' + videoId
					var result_video
					var result_measurement

					const response_v = await fetch(link_video).then(
						response_v => response_v.json().then(
							data => {
								result_video = data
							}
						)
					)

					const response_m = await fetch(link_measurement).then(
						response_m => response_m.json().then(
							data => {
								result_measurement = data
							}
						)
					)

					var format_result = {"video": result_video, "measurement": result_measurement};
					console.log("Work");
					onNewVideo(format_result)
				}}>
					Search
				</Button>
			</Form.Field>
		</Form>
	)
}