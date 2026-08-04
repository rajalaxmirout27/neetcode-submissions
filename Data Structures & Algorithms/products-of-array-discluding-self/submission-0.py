class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        prefix = 1

        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]

        suffix = 1

        for j in range(n-2, -1, -1):
            suffix *= nums[j+1]
            ans[j] *= suffix

        return ans