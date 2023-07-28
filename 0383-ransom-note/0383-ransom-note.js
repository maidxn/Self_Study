/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const magazine_map = new Map();
    for (let i of magazine){
        if (magazine_map.has(i)){
            magazine_map.set(i, magazine_map.get(i) + 1);
        } else {
            magazine_map.set(i, 1);
        }
    }

    const ransomNote_map = new Map();
    for (let i of ransomNote){
        if (ransomNote_map.has(i)){
            ransomNote_map.set(i, ransomNote_map.get(i) + 1);
        } else {
            ransomNote_map.set(i, 1);
        }
    }

    for (let [key, value] of ransomNote_map){
        if (!magazine_map.has(key) || magazine_map.get(key) < ransomNote_map.get(key)){
            return false;
        }
    }   
    return true;
};