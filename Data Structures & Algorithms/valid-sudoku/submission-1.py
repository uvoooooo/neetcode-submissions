class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in board:
            dict = defaultdict(int)
            for x in i:
                dict[x] += 1
                if x != '.' and dict[x] >= 2:
                    return False

        # column

        for y in range(0,9):
            dict_c = defaultdict(int) 
            for x in range(0, 9):
                dict_c[board[x][y]]+= 1
                if board[x][y] != '.' and dict_c[board[x][y]] >= 2:
                    return False


        # sub-box
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                freq = defaultdict(int)

                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):

                        freq[board[i][j]] += 1
                        if board[i][j] != "." and freq[board[i][j]] >= 2:
                            return False

        return True