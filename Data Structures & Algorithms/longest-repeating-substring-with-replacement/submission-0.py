class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxfreq = 0
        res = 0

        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxfreq = max(maxfreq, freq[s[right]])

            window = right-left+1
            replace = window - maxfreq

            if replace > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right-left+1)

        return res