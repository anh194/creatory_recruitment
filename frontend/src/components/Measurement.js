import React, { Component } from 'react';
import { Accordion, Icon } from "semantic-ui-react";


export default class Measurement extends Component {
  state = { activeIndex: 1 }

  handleClick = (e, titleProps) => {
    const { index } = titleProps
    const { activeIndex } = this.state
    const newIndex = activeIndex === index ? -1 : index

    this.setState({ activeIndex: newIndex })

  }

  render() {
    const { activeIndex } = this.state
    if(this.props.measurement){
    	return (
      <Accordion styled style={ { marginTop:40 } }>
        <Accordion.Title
          active={activeIndex === 0}
          index={0}
          onClick={this.handleClick}
        >
          <Icon name='dropdown' />
          Measurement
        </Accordion.Title>
        <Accordion.Content active={activeIndex === 0}>
          	<p> <b>Measure time</b>: {this.props.measurement.time}</p>
			<p> <b>View</b>: {this.props.measurement.view}</p>
			<p> <b>Comment</b>:{this.props.measurement.comment}</p>
			<p> <b>Like</b>: {this.props.measurement.like}</p>
			<p> <b>Dislike</b>: {this.props.measurement.dislike}</p>
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