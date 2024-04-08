class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0 = len([s for s in students if s == 0])
        count1 = len([s for s in students if s == 1])
        prefers = [count0, count1]
        
        for s in sandwiches:
            if prefers[s] <= 0:
                return sum(prefers)
            prefers[s] -= 1
        
        return 0 

        