var express = require('express');
var app = express();

var Animal = require('./Animal.js');
var Toy = require('./Toy.js');

app.use('/', (req, res) => {
	res.json({ msg : 'It works!' });
    });
    
app.use('/findToy', (req, res) => {
	var searchid = req.query.id;
	res.json({ msg : 'It works! in findToy'});
	Toy.findOne( {id: searchid}, (err, Toy) => {
		if (err) {
		    res.type('html').status(500);
		    res.send('Error: ' + err);
		}
		else if (!Toy) {
		    res.type('html').status(200);
		    res.send('No id found ' + searchid);
		}
		else {
		    res.json({ msg : 'It works! in render' });
		    res.render('ToyInfo', {toy: Toy});
		}
	    });
});

app.listen(3000, () => {
	console.log('Listening on port 3000');
    });



// Please do not delete the following line; we need it for testing!
module.exports = app;
