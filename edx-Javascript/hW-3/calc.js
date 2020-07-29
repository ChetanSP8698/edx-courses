/*
 * Implement all your JavaScript in this file!
 */

//"use strict";

numstack = [];
oper = '';
var ext;
var opfl;
var flag;
var eqfl = 1;

$('#button0, #button1, #button2, #button3, #button4, #button5, #button6, #button7, #button8, #button9').click(function() {
	if (flag == 1) {
		$('#display').val('');
		var n = $(this).val();
		$('#display').val($('#display').val() + n);
		flag = 0;
	}
	else {
		flag = 0;
		var n = $(this).val();
		$('#display').val($('#display').val() + n);
	}
	opfl = 0;
});

$('#clearButton').click(function() {
	$('#display').val('');
	oper = '';
	numstack = [];
	flag = 9;
	eqfl = 1;
	opfl = 9;
});

$('#addButton').click(function() {
	if (oper) {
		equal();
		oper = '+';
	}
	else {
		var av = $('#display').val();
		numstack.push(Number(av));
		oper = '+';
	}
	flag = 1;
	opfl = 1;
	eqfl = 1;
});

$('#subtractButton').click(function() {
	if (oper) {
		equal();
		oper = '-';
	}
	else {
		var sv = $('#display').val();
		numstack.push(Number(sv));
		oper = '-';
	}
	flag = 1;
	opfl = 1;
	eqfl = 1;
});

$('#multiplyButton').click(function() {
	if (oper) {
		equal();
		oper = '*';
	}
	else {
		var mv = $('#display').val();
		numstack.push(Number(mv));
		oper = '*';
	}
	flag = 1;
	opfl = 1;
	eqfl = 1;
});

$('#divideButton').click(function() {
	if (oper) {
		equal();
		oper = '/';
	}
	else {
		var dv = $('#display').val();
		numstack.push(Number(dv));
		oper = '/';
	}
	flag = 1;
	opfl = 1;
	eqfl = 1;
});

$('#equalsButton').click(function() {
	equal();
});

function equal() {
	if (opfl == 1) {}
	else {
		var nv = numstack.pop();
		
		if (eqfl == 1) {
			var curr = $('#display').val();
			ext = curr;
			eqfl = 0;
		}
		else {
			curr = Number(ext);
		}
		
		if (oper == '+') {
			var res = Number(nv) + Number(curr);
			$('#display').val(res);
		}
	
		if (oper == '-') {
			var res = Number(nv) - Number(curr);
			if (Number(nv) > Number(curr)) {
				$('#display').val(res);
			}
			else {
				$('#display').val(res);
			}
		}
		
		if (oper == '*') {
			var res = Number(nv) * Number(curr);
			$('#display').val(res);
		}
		
		if (oper == '/') {
			var res = Number(nv) / Number(curr);
			$('#display').val(res);
		}
		flag = 1;
		numstack.push(res);
	}
}	
