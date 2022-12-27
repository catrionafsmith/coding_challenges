// How to change a string into a number

// function makeNumber(str) {
//     return Number(str);
// }

// // can also use:
// function makeNumber(str) {
//     return ParseInt(str)
// }

// How to change lowercase into Uppercase
function makeUpperCase(str) {
    return str.toUpperCase();
  }

//  Reflection - need to remember to include the () at the end of a function in order for it to run.
// Best solutions:
const makeUpperCase = str => str.toUpperCase();
// good reminder of the arrow function in js. str => str.toUpperCase();
// note that makeUpperCase is a constant rather than a function here.  
// or 
function makeUpperCase(str) {return str.toUpperCase();} // When there is only one line inside the {}, 
//you can put it all on the same line