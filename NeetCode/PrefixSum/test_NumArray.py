import unittest
from NumArray import NumArray

class TestNumArray(unittest.TestCase):
    def test_sumRange_basic(self):
        arr = NumArray([1, 2, 3, 4, 5])
        self.assertEqual(arr.sumRange(0, 2), 6)   # 1+2+3
        self.assertEqual(arr.sumRange(1, 3), 9)   # 2+3+4
        self.assertEqual(arr.sumRange(0, 4), 15)  # 1+2+3+4+5

    def test_sumRange_single_element(self):
        arr = NumArray([10, 20, 30])
        self.assertEqual(arr.sumRange(0, 0), 10)
        self.assertEqual(arr.sumRange(1, 1), 20)
        self.assertEqual(arr.sumRange(2, 2), 30)

    def test_sumRange_negative_numbers(self):
        arr = NumArray([-1, -2, -3, -4])
        self.assertEqual(arr.sumRange(0, 3), -10)
        self.assertEqual(arr.sumRange(1, 2), -5)

    def test_sumRange_mixed_numbers(self):
        arr = NumArray([3, -2, 5, -1])
        self.assertEqual(arr.sumRange(0, 3), 5)   # 3-2+5-1
        self.assertEqual(arr.sumRange(1, 2), 3)   # -2+5

    def test_sumRange_entire_array(self):
        arr = NumArray([7])
        self.assertEqual(arr.sumRange(0, 0), 7)

if __name__ == "__main__":
    unittest.main()