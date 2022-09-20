class CheckWinner:
    def __init__(self, game_board):
        self.board = game_board

    def winner(self) -> bool:
        """Returns True if a player won the game."""
        return any([self.hori(), self.vert(), self.diag()])

    def is_tie(self) -> bool:
        """
        Check for a tie by checking if the board is full.
        """
        return '-' not in self.board

    def is_dash(self, position) -> bool:
        """
        Check whether position is a dash.

        :param position: Position to check for a dash.
        """
        return self.board[position] == '-'

    def hori(self) -> bool:
        """
        Check if a player won horizontally.

        :return: Returns True if the player won horizontally.
        """
        out = []
        for row in range(0, 8, 3):
            is_row_equal = self.board[row] == self.board[row + 1] == self.board[row + 2]
            out.append(is_row_equal and not self.is_dash(row))

        return any(out)

    def vert(self) -> bool:
        """
        Check if a player won vertically.

        :return: Returns True if the player won vertically.
        """
        out = []
        for col in range(3):
            is_col_equal = self.board[col] == self.board[col + 3] == self.board[col + 6]
            out.append(is_col_equal and not self.is_dash(col))

        return any(out)

    def diag(self) -> bool:
        """
        Check if a player won diagonally.

        :return: Returns True if the player won diagonally.
        """
        left_to_right = self.board[0] == self.board[4] == self.board[8]  # \
        right_to_left = self.board[2] == self.board[4] == self.board[6]  # /

        return (left_to_right or right_to_left) and not self.is_dash(4)
