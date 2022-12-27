
// 8kyu There was a test in your class and you passed it. Congratulations!
// But you're an ambitious person. You want to know if you're better than the average student in your class.
// You receive an array with your peers' test scores. Now calculate the average and compare your score!
// Return True if you're better, else False!
// Note:
// Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

// My ideas:
// Find the average (including my point)
// Use .length to find the number of scores in the class.
// can return on one line as if the condition is met the line will return true.

// *Initially forgot that classPoints is just an array, not the total of all the scores.
function betterThanAverage(classPoints, yourPoints) {
    return yourPoints > ((classPoints + yourPoints)/(1 + classPoints.length))
  }

// My Submitted solution
function betterThanAverage(classPoints, yourPoints) {
    return yourPoints > (eval(classPoints.join('+')) + yourPoints)/(1 + classPoints.length)
  }

// Other solutions from codewars:
function betterThanAverage(classPoints, yourPoints) {
    return yourPoints > classPoints.reduce((a, b) => a + b, 0) / classPoints.length; 
  }
function betterThanAverage(classPoints, yourPoints) {
    var classAvg = 0;
    for (var i = 0; i < classPoints.length; i++){
        classAvg += classPoints[i]; 
    }
    classAvg = classAvg/classPoints.length; 
    return yourPoints > classAvg;
}