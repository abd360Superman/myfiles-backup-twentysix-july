var numero = 400;
console.log("Number used for all console statments: " + 
	numero)

function makeDivisor(divisor) {
	var myFunc = function(x) {
		return x / divisor;
	};
	return myFunc;
}

var half = makeDivisor(2);
console.log("Half of " + numero + ": " + 
	half(numero));

function makeMultiplier(multiplier) {
	var myFunction = function(x) {
		return x * multiplier;
	}
	return myFunction;
}

var doubleIt = makeMultiplier(2);
console.log("Double of " + numero + ": " + 
	doubleIt(numero));