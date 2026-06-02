# Sort an Array - Merge Sort, Divide and Conquer

You are given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

## Intuition

Merge sort divides the array into two halves, recursively sorts each half, and then merges the sorted halves. The merge step combines two sorted arrays into one, by repetedly picking the smaller element from the front of each array. This divide and conquer approach guarantees O(n log n) time, regardless of input order.

## Approach/Algorithm

1. Base case: if the subarray has one or zero elements, it is already sorted.
2. Find the middle index and recursively sort the left half (`l` to `mid`) and right half (`mid + 1` to `r`).
3. Merge the two sorted halves:
    - Create temporary arrays for `left` and `right` portions.
    - Compare elements from both arrays and place the smaller one into the result.
    - Copy any remaining elements from either array.
4. Return the sort array.

## Complexity

- Time complexity: O(nlogn)
- Space complexity: O(n)

## Code

### Python

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
```

## Notes

[Any additional notes or alternative approaches]
