from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        long_sub_set =[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>long_sub_set[-1]:
                long_sub_set.append(nums[i])
            else:
                index = bisect_left(long_sub_set,nums[i])
                long_sub_set[index] = nums[i]
         
        return len(long_sub_set)