class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        n = len(height)
        j = n-1
        area = 0
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else :
                i += 1
                j -= 1
        return area

# https://leetcode.com/problems/container-with-most-water/        