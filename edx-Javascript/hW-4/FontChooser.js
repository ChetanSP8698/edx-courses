class FontChooser extends React.Component {

    constructor(props) {
	super(props);
	this.state = {hidden : true, bold : !props.bold, size : Number(props.size), color : props.color, defsize : Number(props.size)};
    }
    
    handleClick() {
      this.setState( { hidden : (this.state.hidden == true ? false : true) } );
    }  

    toggle() {
        this.setState({
            bold : !this.state.bold
        });
    }
    
    incrementSize () {
       if (this.state.size >= Number(this.props.max) - 1) {
        	this.setState ({ color : "red"});
        }
        else {
        	this.setState ({color : "black"});
        }
        
    	if (this.state.size < Number(this.props.max)) {
      		this.setState({ 
        		size : this.state.size + 1
        	});
        }
    }
    
    decrementSize () {
    	
    	if (this.state.size > Number(this.props.min)) {
    		this.setState({
    			size : this.state.size - 1
    		});
    	}
    	
    	if (this.state.size <= Number(this.props.min) + 1) {
        	this.setState ({ color : "red"});
        }
        else {
        	this.setState ({color : "black"});
        }
    	
    }
    
    initialValue () {
    	this.setState({
    		size : this.state.defsize
    	});
    }
    
    
    render() {
    
	//var style = this.state.hidden ? {display : 'none'} : {};
	
	var bold = this.state.bold ? 'bold' : 'normal';
	
	//var color = this.state.color;
	
	var nwStyle = {fontSize : this.state.size};
	
	return(
	       <div>
	       <span hidden={this.state.hidden}>
	       <input type="checkbox" id="boldCheckbox" onChange = {this.toggle.bind(this)}/>
	       <button id="decreaseButton" onClick = {this.decrementSize.bind(this)}>-</button>
	       <span id="fontSizeSpan" onDoubleClick={this.initialValue.bind(this)} style={{color:this.state.color}}>{this.state.size}</span>
	       <button id="increaseButton" onClick = {this.incrementSize.bind(this)}>+</button>
	       </span>
	       
	       <span id="textSpan" onClick={this.handleClick.bind(this)} style={Object.assign({}, nwStyle, {fontWeight:bold})}>{this.props.text}</span>
	       </div>
	);
    }
}

