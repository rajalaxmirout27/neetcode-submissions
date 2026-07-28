class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):

            hashmap = {}

            for i in s:
                hashmap[i] = hashmap.get(i, 0) + 1

            hashmap2 = {}

            for i in t:
                hashmap2[i] = hashmap2.get(i, 0) + 1
            
            if hashmap == hashmap2:
                return True

            return False

        return False