class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1

        lmax, rmax = 0, 0

        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])

            if lmax < rmax:
                ans += lmax - height[left]
                left += 1
            else:
                ans += rmax - height[right]
                right -= 1

        return ans