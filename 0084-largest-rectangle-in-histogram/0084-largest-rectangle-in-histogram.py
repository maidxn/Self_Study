class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea = [], 0
        
        for i, h in enumerate(heights+[0]):
            while stack and heights[stack[-1]] > h:
                H = heights[stack.pop()]
                if not stack:
                    W = i 
                else:
                    W = i - stack[-1] - 1
                maxArea = max(maxArea, H * W)
            stack.append(i)
        return maxArea