class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        st_left = []
        left = [-1] * n

        for i in range(n):
            while st_left and heights[st_left[-1]] >= heights[i]:
                st_left.pop()

            if st_left:
                left[i] = st_left[-1]

            st_left.append(i)


        st_right = []
        right = [n] * n

        for i in range(len(heights)-1,-1,-1):
            while st_right and heights[st_right[-1]] >= heights[i]:
                st_right.pop()

            if st_right:
                right[i] = st_right[-1]

            st_right.append(i)


        mx_area = 0

        for i in range(n):
            area = heights[i] * (right[i]-left[i]-1)
            
            mx_area = max(area, mx_area)

        return mx_area