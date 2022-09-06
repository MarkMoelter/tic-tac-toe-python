board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-',
]

def dashes(num_dashes: int) -> str:
    out = ''

    for _ in range(num_dashes):
        out += '-'

    return out


# TODO: print the game board
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(dashes(9))
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(dashes(9))
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# TODO: take player input
def player_input(board, current_player):
    inp = int(input('Enter a number 0-8: '))

    is_board_position = 0 <= inp <= 8
    is_empty = board[inp] == '-'

    if is_board_position and is_empty:
        board[inp] = current_player


# TODO: check for win or tie conditions
class CheckGame:
    def __init__(self, board):
        self.board = board

    def is_dash(self, position) -> bool:
        if self.board[position] == '-':
            return True

    def winner(self):
        winning_player = [self.hori(), self.vert(), self.diag()]
        for ele in winning_player:
            if ele is not None:
                return ele

    def hori(self):
        """
        Check if a player won horizontally.

        :return:
        """
        for row in range(0, 8, 3):
            is_row_equal = self.board[row] == self.board[row + 1] == self.board[row + 2]

            if is_row_equal and not self.is_dash(row):
                return self.board[row]

    def vert(self):
        """
        Check if a player won vertically.

        :return:
        """
        for col in range(3):
            is_col_equal = self.board[col] == self.board[col + 3] == self.board[col + 6]

            if is_col_equal and not self.is_dash(col):
                return self.board[col]

    def diag(self):
        """
        Check if a player won diagonally.

        :return:
        """
        if self.board[0] == self.board[4] == self.board[8] and not self.is_dash(0):
            return self.board[0]

        if self.board[2] == self.board[4] == self.board[6] and not self.is_dash(2):
            return self.board[2]

    def is_tie(self):
        return '-' not in self.board


# TODO: switch the player
# TODO: check for win or tie again

# TODO: game loop runner
def game_loop(is_running=True, current_player='X'):
    while is_running:
        print_board(board)
        player_input(board, current_player)

        if current_player == 'X':
            current_player = 'O'

        elif current_player == 'O':
            current_player = 'X'

        # winner
        if CheckGame(board).winner() is not None:
            is_running = False
            print(f'"{CheckGame(board).winner()}" won!')
            print('Final position: ')
            print_board(board)

        # tie
        if CheckGame(board).is_tie():
            is_running = False
            print('It is a tie!')
            print('Final position: ')
            print_board(board)

    print('Broke out of game loop')


if __name__ == '__main__':
    game_loop()
