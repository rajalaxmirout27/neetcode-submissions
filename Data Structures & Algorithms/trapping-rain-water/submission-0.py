class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        lmax = [0] * n
        rmax = [0] * n

        ans = []

        lmax[0] = height[0]
        rmax[n-1] = height[n-1]

        for i in range(1,n):
            lmax[i] = max(lmax[i-1], height[i])
        
        for j in range(n-2,-1,-1):
            rmax[j] = max(rmax[j+1], height[j])

        for i in range(n):
            ans.append(min(lmax[i], rmax[i]) - height[i])

        return sum(ans)