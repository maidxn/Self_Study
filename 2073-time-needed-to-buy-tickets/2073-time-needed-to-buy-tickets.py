class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        cur = 0
        N = len(tickets)
        
        while tickets[k] > 0:
            if tickets[cur] > 0:
                tickets[cur] -= 1
                time += 1
            cur = cur + 1 if cur + 1 < N else 0
        return time