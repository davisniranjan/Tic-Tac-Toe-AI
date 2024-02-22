import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9

    def print_board(self):
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}')
            if i < 6:
                print('-' * 9)

    def is_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
           if all(cell == player for cell in self.board[i:i+3]):
                return True

        # Check columns
        for i in range(3):
          if all(cell == player for cell in self.board[i::3]):
                return True

        # Check diagonals
        if all(cell == player for cell in self.board[::4]) or all(cell == player for cell in self.board[2:7:2]):
            return True

        return False

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_board_full()

    def get_empty_cells(self):
        return [i for i, val in enumerate(self.board) if val == ' ']

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def minimax(self, depth, maximizing_player):
        if self.is_winner('O'):
            return 1
        elif self.is_winner('X'):
            return -1
        elif self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_empty_cells():
                self.make_move(move, 'O')
                eval = self.minimax(depth + 1, False)
                self.make_move(move, ' ')
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_empty_cells():
                self.make_move(move, 'X')
                eval = self.minimax(depth + 1, True)
                self.make_move(move, ' ')
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self):
        best_score = float('-inf')
        best_move = None

        for move in self.get_empty_cells():
            self.make_move(move, 'O')
            score = self.minimax(0, False)
            self.make_move(move, ' ')

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

def main():
    game = TicTacToe()

    while not game.is_game_over():
        game.print_board()
        player_move = int(input("Enter your move (1-9): ")) - 1

        if player_move not in game.get_empty_cells():
            print("Invalid move. Try again.")
            continue

        game.make_move(player_move, 'X')

        if game.is_game_over():
            break

        print("AI is thinking...")
        ai_move = game.best_move()
        game.make_move(ai_move, 'O')

    game.print_board()

    if game.is_winner('X'):
        print("You win!")
    elif game.is_winner('O'):
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
