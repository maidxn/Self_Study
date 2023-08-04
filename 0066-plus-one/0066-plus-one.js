/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    const res = [];
    let add_up = true;
    for (let i = digits.length - 1; i > -1; i--){
        if (add_up){
            let temp = Number(digits[i]) + 1;
            if (temp < 10){
                res.unshift(temp);
                add_up = false;
            }
            else {
                temp = String(temp)[String(temp).length - 1];
                res.unshift(temp)
            }
        } else {
            res.unshift(digits[i]);
        }
    }
    if (add_up){
        res.unshift(1);
    }
    return res;
};