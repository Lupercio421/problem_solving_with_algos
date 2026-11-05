from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p,s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop(-1) //-1
        print(str(len(stack)))
        return len(stack)
    
solution = Solution()
target = 10
position = [0,4,2]
speed = [2,1,3]
solution.carFleet(target= target, position= position, speed=speed)