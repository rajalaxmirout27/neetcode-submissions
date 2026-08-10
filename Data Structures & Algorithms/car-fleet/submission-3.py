class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        arr = [[None,None] for _ in range(n)]

        for i in range(n):
            arr[i][0] = position[i]
            arr[i][1] = (target - position[i]) / speed[i]

        arr.sort(reverse=True)
        
        count = 0
        prev = 0

        for j in range(len(arr)):

            if arr[j][1] > prev:
                count += 1
                prev = arr[j][1]

        return count