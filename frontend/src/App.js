import React, {useState} from 'react';
import './App.css';
import Videos from "./components/Videos"
import { VideoForm } from "./components/VideoForm"
import Measurement from "./components/Measurement"
import { Container } from "semantic-ui-react";

function App() {
  const [videos, setVideos] = useState();
  const [measurement, setMeasurement] = useState();

  return (
    <div className="App">
    <Container style={ { marginTop: 40} }>
      <VideoForm onNewVideo={result => {
        setVideos(currentVideos => result['video']);
        setMeasurement(currentMeasurement => result['measurement'])
      }}/>
      <Videos videos={videos} />
      <Measurement measurement={measurement} />
    </Container>
    </div>
  );
}

export default App;

