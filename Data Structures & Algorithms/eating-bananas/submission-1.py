class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        mn = 1
        mx = max(piles)

        ans = mx

        while mn <= mx:
            mid = (mn + mx) // 2

            total = 0
            for p in piles:
                total += math.ceil(p/mid)

            if total <= h:
                ans = mid
                mx = mid - 1
            else:
                mn = mid + 1

        return ans

