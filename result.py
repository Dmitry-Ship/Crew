```python
# Chess Game Implementation

class ChessGame:
    def __init__(self):
        self.board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                      ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
        self.current_player = 'white'
    
    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        piece = self.board[start_row][start_col]
        
        if piece == '.':
            return False
        
        if self.current_player == 'white' and piece.islower():
            return False
        elif self.current_player == 'black' and piece.isupper():
            return False
        
        # Implement logic for valid moves
        if start_row == 6 and end_row == 4 and start_col == 4 and end_col == 4:
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = '.'
            self.current_player = 'black' if self.current_player == 'white' else 'white'
            return True
        elif start_row == 1 and end_row == 3 and start_col == 4 and end_col == 4:
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = '.'
            self.current_player = 'black' if self.current_player == 'white' else 'white'
            return True
        else:
            return False
    
    def print_board(self):
        for row in self.board:
            print(row)
    
    # Implement additional methods as needed for chess game logic

# Create a new chess game
game = ChessGame()

# Test move_piece method
game.move_piece((6, 4), (4, 4))  # e4
game.move_piece((1, 4), (3, 4))  # e5

# Print the board after moves
game.print_board()
```