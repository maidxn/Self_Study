class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = {}
        for a in arr:
            dictionary[a] = 1 + dictionary.get(a, 0)
        return True if len(set(dictionary.values())) == len(dictionary) else False