// Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

// Examples:
// Input: 42145 Output: 54421
// Input: 145263 Output: 654321
// Input: 123456789 Output: 987654321

// My ideas:
// Split the number into individual digits, sort the digits and put the number back together.
// split(), sort(), join()?
// Does sort work in js? If not, need to compare each digit and see which is higher.

// This version did not *totally work
// function descendingOrder(n){
//     let digits = n.toString().split('')
//     let sortDig = n.toString().split('').sort().reverse().join('')
//     for (let i=0; i<(digits.length-1); i++) {
//         if (digits[i] < digits[i+1]) {
//             sortDig[i] = digits[i+1];
//             sortDig[i+1] = digits[i]; 
//         } else {
//             sortDig[i] = digits[i];
//             sortDig[i+1] = digits[i+1]
//         }
//     }
//     console.log(sortDig)
//   }

function descendingOrder(n){
    let sortDig = n.toString().split('').sort().reverse().join('')
    console.log(sortDig)
  }

descendingOrder(123456789)



// N.B. Was not strict equal, as the returned number was actually a string. Therefore the final function was:
function descendingOrder(n) {
    return Number(n.toString().split('').sort().reverse().join(''))
  }


// Alternatives on CodeWars:
// function descendingOrder(n){
//     return +(n + '').split('').sort(function(a,b){ return b - a }).join('');
//   }