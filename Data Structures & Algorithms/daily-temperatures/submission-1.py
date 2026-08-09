class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        st = []
        arr = [0] * n

        for t in range(n-1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[t]:
                st.pop()
            if st:
                arr[t] = st[-1] - t
            st.append(t)

        return arr