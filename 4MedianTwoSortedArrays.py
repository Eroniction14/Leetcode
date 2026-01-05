class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        l=len(nums3)
        mid=l//2

        if l % 2 == 1:
            return float(nums3[mid])
        else:
            return float((nums3[mid]+nums3[mid-1])/2)
