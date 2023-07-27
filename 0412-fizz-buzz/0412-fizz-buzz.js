/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    var answers = [];
    for (let i = 1; i < n + 1; i++){
        let answer = String(i);
        if (i % 5 === 0 && i % 3 === 0){
            answer = "FizzBuzz";
        } else if (i % 3 === 0){
            answer = "Fizz";
        } else if (i % 5 === 0) {
            answer = "Buzz";
        }
        answers.push(answer);
    }
    return answers;
};