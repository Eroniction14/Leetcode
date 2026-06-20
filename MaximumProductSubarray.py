class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = curr_max = current = nums[0]
        for i in range(1,len(nums)):
            a=curr_max
            curr_max = max(a * nums[i], curr_min * nums[i], nums[i])
            curr_min = min(a * nums[i], curr_min * nums[i], nums[i])
            current = max(curr_max,current)
            
        return current
