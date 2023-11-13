from check_winner import CheckWinner


class TicTacToe:
    def __init__(self):
        self.board = [
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
        ]

    @staticmethod
    def dashes(num_dashes: int) -> str:
        """
        Returns a string containing the number of hyphens specified.

        :param num_dashes: How many hyphens to add to the string.
        :return: The string of hyphens.
        """
        out = ""
        for _ in range(num_dashes):
            out += "-"
        return out

    def print_board(self):
        """
        Print the board in the terminal.
        """
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.dashes(9))
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.dashes(9))
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def player_input(self, current_player) -> None:
        """
        Take the player's input and put in on the board.
        Repeats until the player enters a valid state.

        :param current_player: The character of the current player.
        """
        while True:
            player_input = int(input(f'"{current_player}", enter a number 0-8: '))

            is_board_position = 0 <= player_input <= 8
            is_empty = self.board[player_input] == "-"

            if is_board_position and is_empty:
                self.board[player_input] = current_player
                break
            else:
                print(f'"{player_input}" is not a valid board position.')

    def play_game(self, current_player="X"):
        """
        Main loop for Tic Tac Toe.
        Print the current board state,
        then asks for the current player's input,
        then checks for wins or ties,
        finally swaps the current player.
        """
        while True:
            self.print_board()
            self.player_input(current_player)

            game = CheckWinner(self.board)
            # winner
            if game.winner():
                print(f'"{current_player}" won!')
                print("Final position: ")
                self.print_board()
                break

            # tie
            elif game.is_tie():
                print("It is a tie!")
                print("Final position: ")
                self.print_board()
                break

            if current_player == "X":
                current_player = "O"
            elif current_player == "O":
                current_player = "X"
