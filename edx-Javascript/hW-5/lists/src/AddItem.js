import React, { Component } from 'react';

class AddItem extends Component {

  constructor() {
    super();
    this.state = {
    }
  }

  handleSubmit(e) {
      e.preventDefault(); // this prevents the page from reloading -- do not delete this line!
      
	if(this.refs.id.value === '') {
      		alert('Title is required');
    	} 
    	else {
      		this.setState({items:
      		        this.refs.id.value
      	}, function() {
        	console.log(this.state);
        	this.props.addItem(this.state.items);
      	});
    	}
      // Implement the rest of this function here!
  }
    

  render() {
    var divName = 'add' + this.props.idName;
    return (
      <div className='addItemDiv'>
      <h4>Add {this.props.idName}</h4>
      <form ref='form' onSubmit={this.handleSubmit.bind(this)}>
      <div id={divName} ref={divName}>
        <label>Name</label><br />
        <input type='text' ref='id' />
        </div>
        <br />
        <input type='submit' value='Submit' />
        <br />
      </form>
      </div>
    );
  }

}

export default AddItem;
