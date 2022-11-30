// 8kyu Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
// My ideas:
// Use a for loop
// Concatenate a string
// Is there a way to make it on one line?

function repeatStr (n, s) {
    let newStr =""
    for(i=0; i<n; i++) {
      newStr += s
    }
    return newStr;
  }

// Solutions from CodeWars - there is a repeat function!:
function repeatStr (n, s) {
    return s.repeat(n)
}

repeatStr = (n, s) => s.repeat(n)