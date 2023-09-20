class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n-2):
            low, hi = i+1, n-1
            while low < hi:
                sum = nums[i] + nums[low] + nums[hi]
                if(sum == target) :
                    return sum
                elif(sum > target) :
                    hi -= 1
                else :
                    low += 1
                if abs(target - sum) < abs(target - res):
                    res = sum
        return res
# https://leetcode.com/problems/3sum-closest/