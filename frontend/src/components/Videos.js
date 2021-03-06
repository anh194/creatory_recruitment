import React, { Component } from 'react';
import { Accordion, Icon } from "semantic-ui-react";

export default class Videos extends Component {
  state = { activeIndex: 1 }

  handleClick = (e, titleProps) => {
    const { index } = titleProps
    const { activeIndex } = this.state
    const newIndex = activeIndex === index ? -1 : index

    this.setState({ activeIndex: newIndex })

  }

  render() {
    const { activeIndex } = this.state
    if(this.props.videos){
    	return (
      <Accordion styled style={ { marginTop: 40} }>
        <Accordion.Title
          active={activeIndex === 0}
          index={0}
          onClick={this.handleClick}
        >
          <Icon name='dropdown' />
          {this.props.videos.title}
        </Accordion.Title>
        <Accordion.Content active={activeIndex === 0}>
          	<p> <b>Date</b>: {this.props.videos.date}</p>
			<p> <b>Duration</b>: {this.props.videos.duration}</p>
			<p> <b>Channel ID</b>:{this.props.videos.channel_id}</p>
			<p> <b>Youtube ID</b>: {this.props.videos.youtube_id}</p>
			<p> <b>Description</b>: {this.props.videos.description}</p>
        </Accordion.Content>

      </Accordion>
    )
    }else{
    	return(
    		<p></p>
    	)
    }
  }
}