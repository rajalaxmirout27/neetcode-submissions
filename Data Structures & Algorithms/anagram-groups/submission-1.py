class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            key = [0] * 26

            for char in word:
                idx = ord(char) - ord("a")
                key[idx] += 1

            key = tuple(key)

            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(word)

        return list(hashmap.values())