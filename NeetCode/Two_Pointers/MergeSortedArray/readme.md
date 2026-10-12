# Merge Sorted Array - Two Pointers

You are given two integer arrays `nums1` and `nums2`, both sorted in **non-decreasing order**, along with two integers `m` and `n`, where:

- `m` is the number of valid elements in `nums1`,

- `n` is the number of elements in `nums2`.

The array `nums1` has a total length of `(m+n)`, with the first `m` elements containing the values to be merged, and the last `n` elements set to `0` as placeholders.

Your task is to merge the two arrays such that the final merged array is also sorted in **non-decreasing order** and stored entirely within `nums1`.
You must modify nums1 in-place and do not return anything from the function.## Intuition

```text
Example 1:

Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

Output: [1,2,10,20,20,40]
```

## Intuition - Sorting

Using Java's `Arrays.sort()` would help solve half the problem. The other half of the problem would be to begin replacing the `0` of the `nums1` array. `n` helps tell us the number of elements in `nums2`. So we can place those `nums2` elements in `nums1` by begining at `i + m`, where `i` is the counter starting at `0` of a for loop.

## Approach - Sorting

1. Copy all `n` elements from `nums2` into `nums1` starting at index `m`.
2. Sort `nums1` in place.

## Complexity

- Time complexity: O((m+n)log(m+n))
    - Where `m` and `n` represent the number of elements in the arrays `nums1` and `nums2`, respectively
- Space complexity: O(1) or O(m+n) depending on the sorting algorithm.

## Intuition - Three Pointers with Extra Space

Since both arrays are already sorted, we can merge them in linear time using the standard merge technique from merge sort. However, if we write directly into `nums1` from the front, we risk overwriting elements we still need. To avoid this, we first copy the original elements of `nums1` to a temporary array, then merge from both sources into `nums1`.

## Approach - Three Pointers with Extra Space

1. Create a copy of the first `m` elements of `nums1`.
2. Use three pointers: `i` for the copy of `nums1`, `j` for `nums2`, and `idx` for the write position in `nums1`.
3. Compare elements from both sources and write the smaller element to `nums1[idx]`.
4. Increment the corresponding pointer and `idx`.
5. Continue until all elements from both sources are placed.

## Code

<details>

<summary>Java - Sorting</summary>

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = 0; i < n; i++){
            nums1[i+m] = nums2[i];
        }
        Arrays.sort(nums1);
    }
}
```
</details>

<details>

<summary>Java - Three Pointers with Extra Space</summary>

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums1Copy = Arrays.copyOf(nums1, m);
        int idx = 0, i = 0, j = 0;

        while (idx < m + n){ //m + n is the count of valid elements
            //why is `j >= n` needed? 
            // It helps to not read pas the end of nums2

            //How do we help compare if an element of nums2 is greater than the element of nums1Copy at i
            //nums1Copy element at i already being compared to nums2 element at j
            // When that is not the case, we execute the else statement
            if (j >= n || (i < m && nums1Copy[i] <= nums2[j])){
                nums1[idx++] = nums1Copy[i++];
            } else {
                nums1[idx++] = nums2[j++];
            }
        }
    }
}
```
</details>

## Notes

[Any additional notes or alternative approaches]