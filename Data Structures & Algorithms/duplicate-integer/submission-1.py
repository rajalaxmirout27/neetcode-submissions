class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # lst = []

        # for i in nums:
        #     if i in lst:
        #         return True
        #     lst.append(i)

        # return False

        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        for i in hashmap:
            if hashmap[i] > 1:
                return True

        return False