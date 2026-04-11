# Range Sum Query 2D Immutable

You are given a 2D matrix `matrix`, handle multiple queries of the following type:

- Calculate the `sum` of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.
- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the sum of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.
You must design an algorithm where `sumRegion` works on `O(1)` time complexity.

Example:

![2D matrix with a highlighted rectangle showing row1, col1 at upper left corner and row2, col2 at lower right corner, demonstrating the region for which sum is calculated](../images/rectangle_example.jpg)

## Intuition

[Explain your initial approach and thought process]

## Approach

[Detailed steps of your solution strategy]

1. a
    - b
2. c
    - d
        - e

## Complexity

- Time complexity: O(?)
- Space complexity: O(?)

## Code

### Java

```java
class NumMatrix {
    private int[][] sumMat;

    public NumMatrix(int[][] matrix) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;
        sumMat = new int[ROWS + 1][COLS + 1];

        for (int r = 0; r < ROWS; r++){
            int prefix = 0;
            for (int c = 0; c < COLS; c++){
                prefix += matrix[r][c];
                int above = sumMat[r][c + 1];
                sumMat[r + 1][c + 1] = prefix + above;
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        row1++; col1++; row2++; col2++;
        int bottomRight = sumMat[row2][col2];
        int above = sumMat[row1 - 1][col2];
        int left = sumMat[row2][col1 - 1];
        int topLeft = sumMat[row1 - 1][col1 - 1];
        return bottomRight - above - left + topLeft;
    }
}
```

### Python

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]
        
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        
        return bottomRight - above - left + topLeft

```

## Notes
