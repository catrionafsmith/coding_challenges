// Check to see if a string has the same amount of 'x's and 'o's. 
// The method must return a boolean and be case insensitive. 
// The string can contain any char.

// My ideas:
// Could use count
// Needs to be case insensitive
// Needs to return a boolean so could just have a conditional statement on the return line
// ***Remember to put strings in ""!
// could use a regex


// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

function XO(str) {
    console.log(str.replace(/[^xX]/g, '').length == str.replace(/[^oO]/g, '').length)
    return (str.replace(/[^xX]/g, '').length == str.replace(/[^oO]/g, '').length)
}
XO("zzoo")

// Other People's Solutions:
// make the string lower case, then split the string wherever there's an x, then count the number of parts it's split into and see if it's the same for the o's.
const XO = str => {
    str = str.toLowerCase().split('');
    return str.filter(x => x === 'x').length === str.filter(x => x === 'o').length;
  }

// Using match and regex to find the number of Xs and Oc - N.B. gi means global and case insensitive.
function XO(str) {
  let x = str.match(/x/gi);
  let o = str.match(/o/gi);
  return (x && x.length) === (o && o.length);
}


