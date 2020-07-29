class FontChooser extends React.Component {

    constructor(props) {
	super(props);
	this.state = {hidden : true, bold : props.bold, size : Number(props.size), color : 'black', defsize : Number(props.size)};
    }
    
    handleClick() {
      this.setState( { hidden : !this.state.hidden } );
    }  

    toggle() {
        this.setState({
            //bold : !this.state.bold
            bold : (this.state.bold == 'true' ? 'false' : 'true')
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
	
	//var bold = this.state.bold ? 'bold' : 'normal';
	var bold = this.state.bold == 'true' ? 'bold' : 'normal';
	//var color = this.state.color;
	
	var nwStyle = {fontSize : this.state.size};
	
	return(
	       <div>
	       <div hidden={this.state.hidden}>
	       <input type="checkbox" id="boldCheckbox" checked={this.state.bold} onChange = {this.toggle.bind(this)} hidden={this.state.hidden}/>
	       <button id="decreaseButton" onClick = {this.decrementSize.bind(this)} hidden={this.state.hidden}>-</button>
	       <span id="fontSizeSpan" onDoubleClick={this.initialValue.bind(this)} style={{color:this.state.color}} hidden={this.state.hidden}>{this.state.size}</span>
	       <button id="increaseButton" onClick = {this.incrementSize.bind(this)} hidden={this.state.hidden}>+</button>
	       </div>
	       
	       <span id="textSpan" onClick={this.handleClick.bind(this)} style={Object.assign({}, nwStyle, {fontWeight:bold})}>{this.props.text}</span>
	       </div>
	);
    }
}


