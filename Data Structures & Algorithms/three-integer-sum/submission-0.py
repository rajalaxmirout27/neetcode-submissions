class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        lst = []

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0 and [nums[i], nums[left], nums[right]] not in lst :
                    lst.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return lst