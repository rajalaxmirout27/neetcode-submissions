class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, ans = [], []

        for i in strs:
            sizes.append(len(i))
        
        for s in sizes:
            ans.append(str(s))
            ans.append(',')
        ans.append('#')
        ans.extend(strs)
        return ''.join(ans)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        idx = s.index("#")

        size_part = s[:idx]
        str_part = s[idx+1:]

        sizes = []

        for i in size_part.split(','):
            if i != "":
                sizes.append(int(i))

        ans = []
        start = 0

        for j in sizes:
            ans.append(str_part[start : start+j])
            start += j

        return ans