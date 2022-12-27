// Return the number (count) of vowels in the given string.
// My ideas:
// use count()?
// Remember to put strings in ""
// Use ternary operator?
// use regex
// remove all the other characters and count what's left

function getCount(str) {
    vowCount = str.replace(/[^aeiou]/g, "").length
    console.log(vowCount)
    return vowCount
}
getCount("abracadavebra")

// More basic version using for loops and if statements.
function getCount(str) {
    let vowNum = 0
    for (let i = 0; i < str.length; i++) {
        if (str[i] == "a" || str[i]  == "e" || str[i] == "i" || str[i] == "o" || str[i] == "u")  {
            vowNum +=1;
        }
    }
  console.log(vowNum)
  return vowNum;
}
getCount("abracadavebra")
// N.B. Put the || inside the if statement.
// Could also use vowNum++ to add on one.