class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0
        next = curr + 1
        while next < len(nums) and curr < len(nums):

            while next < len(nums) and nums[next] == nums[curr]:
                # curr = curr + 1
                next = next + 1

            if (curr + 1 < len(nums) and next < len(nums)):
                curr = curr + 1
                nums[curr] = nums[next]
            next = next + 1
        return curr + 1
