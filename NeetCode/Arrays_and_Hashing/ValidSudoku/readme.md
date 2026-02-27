# Valid Sudoku - DefaultDict/HashTable and Arrays - Medium

You are given a `9 x 9` Sudoku board board. A Sudoku board is valid if the following rules are followed:

1. Each row must contain the digits 1-9 without duplicates.
2. Each column must contain the digits 1-9 without duplicates.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without duplicates.
Return `true` if the Sudoku board is valid, otherwise return `false`

Note: A board does not need to be full or be solvable to be valid

## Intuition

[Explain your initial approach and thought process]

## Approach

[Detailed steps of your solution strategy]

- Step 1
- Step 2
- Step 3

## Complexity

- Time complexity: O(?)
- Space complexity: O(?)

## Code

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
```

## Notes

[Any additional notes or alternative approaches]
