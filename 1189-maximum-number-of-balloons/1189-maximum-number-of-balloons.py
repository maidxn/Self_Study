class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dictionary = {
            'b': [1, 0],
            'a': [1, 0],
            'l': [2, 0],
            'o': [2, 0],
            'n': [1, 0]
        }
        for char in text:
            if char in dictionary:
                dictionary[char][1] += 1
        res = float("inf")
        for each in dictionary:
            word = dictionary[each][1] // dictionary[each][0]
            res = min(res, word)
        return res
        