class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(0, n-2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                low, hi = i+1, n-1
                sum = -nums[i]
                while(low < hi) :
                    if nums[low] + nums[hi] == sum:
                        res.append([nums[i], nums[low], nums[hi]])
                        while (low<hi and nums[low]==nums[low+1]):
                            low+=1
                        while (low<hi and nums[hi] == nums[hi-1]):
                            hi-=1
                        low+=1
                        hi-=1
                    elif sum > nums[low] + nums[hi]:
                        low+=1
                    else :
                        hi-=1
        return res
# https://leetcode.com/problems/3sum/description/