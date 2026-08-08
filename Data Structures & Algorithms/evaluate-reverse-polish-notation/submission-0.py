class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
    
        for t in tokens:
            if t not in "+-*/":
                st.append(int(t))
            
            else:
                b = st.pop()
                a = st.pop()

                if t == "+":
                    st.append(a + b)

                elif t == "-":
                    st.append(a-b)

                elif t == "*":
                    st.append(a*b)

                elif t == "/":
                    st.append(int(a/b))

        return st[-1]