class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_middle_square(self, board):
        return board[4]

    def level_2_number_of_o(self, board):
        return board.count('O')

    def level_3_does_o_have_3_in_a_row(self, board):
        three_o = ['O', 'O', 'O']

        return \
            board[:3] == three_o or \
            board[3:6] == three_o or \
            board[6:] == three_o or \
 \
            board[0::3] == three_o or \
            board[1::3] == three_o or \
            board[2::3] == three_o or \
 \
            board[0::4] == three_o or \
            board[2:8:2] == three_o
