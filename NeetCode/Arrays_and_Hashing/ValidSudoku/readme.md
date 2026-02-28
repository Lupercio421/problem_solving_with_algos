# Valid Sudoku - DefaultDict/HashTable and Arrays - Medium

You are given a `9 x 9` Sudoku board board. A Sudoku board is valid if the following rules are followed:

1. Each row must contain the digits 1-9 without duplicates.
2. Each column must contain the digits 1-9 without duplicates.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without duplicates.
Return `true` if the Sudoku board is valid, otherwise return `false`

Note: A board does not need to be full or be solvable to be valid

## Intuition

For each cell, we can check whether the digit has appeared in:

1. the same `row`

2. the same `column`

3. the same `3x3 box`

We can track the three above using individual hash sets:

- `rows[r]` keeps digits seen in row `r`

- `cols[c]` keeps the digits seen in the column `c`

- `squares[(r // 3, c // 3)]` keeps the digits in the 3x3 box

As soon as the digit appears in any one of the three places (conditional `or`), the board is invalid.

## Approach

- 1. Create three hash maps of sets:
  - 1.1 `rows` to track the digits in each row
  - 1.2 `cols` to track the digits in each col
  - 1.3 `squares` to track digits in each 3x3 sub-box, keyed by `(r // 3, c // 3)`
- 2. Loop through ever cell in the board. You can do a `range(9)` since the board is guaranteed to be of size `3x3`
  - 2.1 Skip the cell if it contains `"."`
  - 2.2. Let `val` be the digit in the cell, which can be retrieved with `board[x][y]`
  - 2.3 If `val` is already in
    - `rows[r]` -> duplicate in the row
    - `cols[c]` -> duplicate in the column
    - `squares[(r // 3, c // 3)]` -> duplicate in the 3x3 box
    - We have a duplicate, return `False`

- 3. Otherwise, add the digit to all the three sets:
  - `rows[r]`
  - `cols[c]`
  - `squares[(r // 3, c // 3)]`

- 4. If the whole board is scanned without a detected duplicate, return `True`.

## Complexity

- Time complexity: O(n**2)
- Space complexity: O(n**2)

## Code

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r/3, c/3)         

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                #rows[r] represents a set
                #cols[c] represents a set
                #squares[(r // 3, c // 3)] represents a set
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
```

```java
public class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<String, Set<Character>> squares = new HashMap<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                String squareKey = (r / 3) + "," + (c / 3);

                if (rows.computeIfAbsent(r, k -> new HashSet<>()).contains(board[r][c]) ||
                    cols.computeIfAbsent(c, k -> new HashSet<>()).contains(board[r][c]) ||
                    squares.computeIfAbsent(squareKey, k -> new HashSet<>()).contains(board[r][c])) {
                    return false;
                }

                rows.get(r).add(board[r][c]);
                cols.get(c).add(board[r][c]);
                squares.get(squareKey).add(board[r][c]);
            }
        }
        return true;
    }
}
```

## Notes
