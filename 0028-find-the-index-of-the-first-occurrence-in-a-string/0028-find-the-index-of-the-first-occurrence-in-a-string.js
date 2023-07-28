/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let index = 0;
    let result = -1;
    while (index < haystack.length){
        if (haystack[index] == needle[0]){
            if (haystack.slice(index, index + needle.length) == needle){
                result = index;
                break;
            }
        }
        index += 1;
    }
    return result;
};