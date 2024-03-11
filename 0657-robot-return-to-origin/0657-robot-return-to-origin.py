class Solution:
    def judgeCircle(self, moves: str) -> bool:
        steps = {"U": 0,
                "D": 0,
                "L": 0,
                "R": 0}
        for move in moves:
            steps[move] += 1
        if steps["L"] == steps["R"] and steps["U"] == steps["D"]:
            return True
        return False
        
        