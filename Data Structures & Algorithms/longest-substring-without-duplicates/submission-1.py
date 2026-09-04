class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        st = ""
        res = 0

        for i in s:
            if i not in st:
                st += i
                res = max(res, len(st))
            else:
                st = st[st.index(i) + 1:]
                st += i

        return res