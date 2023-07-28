/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let head = 0;
    let tail = -1;
    const string = String(x)
    while(head < string.length){
        if (string.at(head) !== string.at(tail)){
            return false;
        }
        head += 1;
        tail -= 1;
    }
    return true;
};