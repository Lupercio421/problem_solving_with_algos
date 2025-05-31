from typing import List
from venv import logger


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        prefixRight = self.prefix[right]
        logger.info(f"prefixRight: {prefixRight}, right: {right}")
        prefixLeft = self.prefix[left-1] if left > 0 else 0
        logger.info(f"prefixLeft: {prefixLeft}, left: {left}")
        return (prefixRight - prefixLeft)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
