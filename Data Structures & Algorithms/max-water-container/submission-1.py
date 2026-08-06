class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = float('-inf')

        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            ht = min(heights[left], heights[right])
            area = width * ht

            ans = max(area, ans)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans