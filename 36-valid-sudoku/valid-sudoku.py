class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(list)
        columns = collections.defaultdict(list)
        squares = collections.defaultdict(list)

        for i in range(9):
            for j in range(9):
                cell_value = board[i][j]
                if cell_value == ".":
                    continue
                rows[i].append(cell_value)
                columns[j].append(cell_value)
                square_index = (i//3) * 3 + (j//3)
                squares[square_index].append(cell_value)

        for group in (rows,columns,squares):
            for area in group.values():
                if len(area) != len(set(area)):
                    return False
        return True