/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const hash_map = new Map();
    for (num of nums) {
        if (hash_map.has(num)){
            return true;
        }
        hash_map.set(num, 1);
    }
    return false;
    
}
