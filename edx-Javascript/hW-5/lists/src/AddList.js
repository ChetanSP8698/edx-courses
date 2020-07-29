import React, { Component } from 'react';

class AddList extends Component {
  constructor() {
    super();
    this.state = {
    };
  }


  handleSubmit(e) {
      	e.preventDefault(); // this prevents the page from reloading -- do not delete this line!
	
	if(this.refs.id.value === '') {
      		alert('Title is required');
    	} 
    	else {
      		this.setState({lists:
        		this.refs.id.value
      	}, function() {
        	//console.log(this.state);
        	this.props.addList(this.state.lists);
      	});
    	}
      // Implement the rest of this function here!
  }

  render() {
    return (
      <div id="addListDiv">
      <form onSubmit={this.handleSubmit.bind(this)}>
      <div id='addList'>
      <label>What will be on your next list?&nbsp;
      <input type='text' ref='id' id='newID'></input>
      </label>
      </div><br />
      <input type='submit' value='Create List' />
      </form>
      </div>
    );
  }
}

export default AddList;
