import React, {useEffect, useState} from 'react';
import './App.css';
import { Videos } from "./components/Videos"
import { VideoForm } from "./components/VideoForm"
import { Container } from "semantic-ui-react";

function App() {
  const [videos, setVideos] = useState();

  // useEffect(() => {
  //   fetch("/video?video_id=FiFUGE3_kqY").then(response =>
  //     response.json().then(data => {
  //       setVideos(data);
  //       console.log(videos);
  //       console.log(data);
  //     })
  //   );
  // }, []); 

  // console.log(videos)

  //<Videos videos={videos} />

  return (
    <div className="App">
    <Container style={ { marginTop: 40} }>
      <VideoForm onNewVideo={video => setVideos(currentVideos => video)}/>
      <Videos videos={videos} />
    </Container>
    </div>
  );
}
export default App;
