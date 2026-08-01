class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        # Initialize the sets with the initial board values
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    box_row = i // 3
                    box_col = j // 3
                    boxes[box_row][box_col].add(num)

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        box_row = i // 3
                        box_col = j // 3
                        for num in range(1, 10):
                            if (num not in rows[i] and
                                num not in cols[j] and
                                num not in boxes[box_row][box_col]):
                                # Place the number
                                rows[i].add(num)
                                cols[j].add(num)
                                boxes[box_row][box_col].add(num)
                                board[i][j] = str(num)

                                if backtrack():
                                    return True

                                # Remove the number (backtrack)
                                rows[i].remove(num)
                                cols[j].remove(num)
                                boxes[box_row][box_col].remove(num)
                                board[i][j] = '.'
                        return False
            return True

        backtrack()