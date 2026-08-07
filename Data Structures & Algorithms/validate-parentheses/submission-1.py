class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        paren = {")":"(", "}":"{", "]":"["}

        for i in s:
            if i == '(' or i == '{' or i == "[":
                st.append(i)
            elif not st or paren[i] != st[-1]:
                return False
            else:
                st.pop()

        return len(st) == 0