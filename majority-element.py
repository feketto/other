class Solution:
    def majorityElement(self, nums):
        nums.sort()
        print(nums)
        index = len(nums) // 2
        return nums[index]

s = Solution()
print(s.majorityElement(nums = [2,2,1,1,1,2,2]))