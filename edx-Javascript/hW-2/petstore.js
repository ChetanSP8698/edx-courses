
/**
 * This function should calculate the total amount of pet food that should be
 * ordered for the upcoming week.
 * @param numAnimals the number of animals in the store
 * @param avgFood the average amount of food (in kilograms) eaten by the animals
 * 				each week
 * @return the total amount of pet food that should be ordered for the upcoming
 * 				 week, or -1 if the numAnimals or avgFood are less than 0 or non-numeric
 */
function calculateFoodOrder(numAnimals, avgFood) {
    // IMPLEMENT THIS FUNCTION!
    nA = Number(numAnimals);
    aF = Number(avgFood);
    if (nA < 0) {
    	return -1;
    }
    
    if (aF < 0) {
    	return -1;
    }
    
    var FoodOrder;
    
    if(isNaN(nA) || isNaN(aF)) {
    	return -1;
    }
    else {
	FoodOrder = nA * aF;
	return FoodOrder;
    }
}

/**
 * Determines which day of the week had the most nnumber of people visiting the
 * pet store. If more than one day of the week has the same, highest amount of
 * traffic, an array containing the days (in any order) should be returned.
 * (ex. ["Wednesday", "Thursday"]). If the input is null or an empty array, the function
 * should return null.
 * @param week an array of Weekday objects
 * @return a string containing the name of the most popular day of the week if there is only one most popular day, and an array of the strings containing the names of the most popular days if there are more than one that are most popular
 */
function mostPopularDays(week) {
    // IMPLEMENT THIS FUNCTION!
    if (week == null || week == []) {
    	return null;
    }
    
    var max = -1;
    var len = week.length;
    var populardays = [];
    
    //Math.max.apply(null, week);
    
    for (var i = 0; i < len; i++) {
    	if (week[i].traffic > max) {
    		max = week[i].traffic;
    	}
    }
    
    for (var j = 0; j < len; j++) {
    	if (max == week[j].traffic) {
    		populardays.push(week[j].name);
    	}
    }
    
    if (populardays.length == 1) {
    	return populardays[0];
    }
    else {
    	return populardays;
    }
}


/**
 * Given three arrays of equal length containing information about a list of
 * animals - where names[i], types[i], and breeds[i] all relate to a single
 * animal - return an array of Animal objects constructed from the provided
 * info.
 * @param names the array of animal names
 * @param types the array of animal types (ex. "Dog", "Cat", "Bird")
 * @param breeds the array of animal breeds
 * @return an array of Animal objects containing the animals' information, or an
 *         empty array if the array's lengths are unequal or zero, or if any array is null.
 */
function createAnimalObjects(names, types, breeds) {
    // IMPLEMENT THIS FUNCTION!
    var animalobj = new Array();
    
    var n = names.length;
    var t = types.length;
    var b = breeds.length;
    
    if(n != t) {
    	return animalobj;
    }
    else {
    	if(n != b) {
    		return animalobj;
    	}
    }
    
    if (n == 0) {
    	return animalobj;
    }
    if (t == 0) {
    	return animalobj;
    }
    if (b == 0) {
    	return animalobj;
    }
    if (names == null) {
    	return animalobj;
    }
    if (types == null) {
    	return animalobj;
    }
    if (breeds == null) {
    	return animalobj;
    }
    
    for (var i = 0; i < n; ++i) {
    	animalobj.push(new Animal(names[i], types[i], breeds[i]));
    }
    
    return animalobj;
}

/////////////////////////////////////////////////////////////////
//
//  Do not change any code below here!
//
/////////////////////////////////////////////////////////////////


/**
 * A prototype to create Weekday objects
 */
function Weekday (name, traffic) {
    this.name = name;
    this.traffic = traffic;
}

/**
 * A prototype to create Item objects
 */
function Item (name, barcode, sellingPrice, buyingPrice) {
     this.name = name;
     this.barcode = barcode;
     this.sellingPrice = sellingPrice;
     this.buyingPrice = buyingPrice;
}
 /**
  * A prototype to create Animal objects
  */
function Animal (name, type, breed) {
    this.name = name;
     this.type = type;
     this.breed = breed;
}


/**
 * Use this function to test whether you are able to run JavaScript
 * from your browser's console.
 */
function helloworld() {
    return 'hello world!';
}



