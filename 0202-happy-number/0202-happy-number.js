/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let number = n;
    while (number >= 10){
        let temp = 0;
        for (const digit of String(number)){
            temp += Number(digit) ** 2;
        }
        number = temp;
    }
    if (number == 1 || number == 7){
        return true;
    }
    return false;
};