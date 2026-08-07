class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        total_sum= sum(nums)
        n = len(nums)

        for i in range(n):
            right_sum= total_sum - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            else:
                left_sum+=nums[i]
        return -1
        