import random


# Constant Token Values
UNPLAYED = ' '
PLAYER1 = 'X'
PLAYER2 = 'O'

class TicTacToe:
    """
    Representation of a Tic Tac Toe game with functions
    for advancing the game through player input or built in AI, 
    testing state and winning conditions.  Use function get_constants()
    to get the tokens to use for player paramters and makring board state.
    
    """
    
    def __init__(self):
        """
        Initialize TicTacToe data board as smashed 1-D list.
        Reference row1: board[0-2], row2: board[3-5] and row3: board[6-8]
        
        """
        self.board = [UNPLAYED, UNPLAYED, UNPLAYED, UNPLAYED, UNPLAYED, 
            UNPLAYED, UNPLAYED, UNPLAYED, UNPLAYED]
    # End Def
    
    def new_game(self):
        """
        Clear state of current game board
        
        """
        for x in range(9):
            self.board[x] = UNPLAYED
    # End Def
    
    def get_board(self):
        """
        Returns the class data board which stores the board data.
        This will be useful for passing board data to a visualizer component.
        """
        return self.board
    # End Def
    
    def get_constants(self):
        """
        Returns a list of the constants used by TicTacToe.
        [UNPLAYED, PLAYER1, PLAYER2]
        
        """
        return [UNPLAYED, PLAYER1, PLAYER2]
    # End Def

    def winner(self):
        """
        Determine if one player has won the game. 
        Returns List [PLAYER, winning_row] or None
        
        """
        winners = [    [0,1,2],[3,4,5],[6,7,8],    # verticals
                       [0,3,6],[1,4,7],[2,5,8],    # horizontals
                       [0,4,8],[2,4,6] ]           # diagonals

        # Test winning conditions and return on winner
        for winner in winners:
            if self.board[winner[0]] != UNPLAYED:
                if self.board[winner[0]] == self.board[winner[1]]:
                    if self.board[winner[1]] == self.board[winner[2]]:
                        return [self.board[winner[2]], winner]

        # No winner, return None
        return None
    # End Def

    def game_over(self):
        """
        Determine if the game has ended (by winner or by cats game)
        Returns either True or False
        
        """
        if self.winner():
            return True
        for position in self.board:
            if position == UNPLAYED:
                return False
        return True
    # End Def

    def move(self, position, player):
        """
        Makes a move at @param (int)position for @param player.
        Valid moves are: [0-8] and correspond to labeling the tic-tac-toe
        board from left to right, top to bottom. 
        Returns True if move is successful otherwise returns False
        
        """
        # Bounds Check
        if position not in range(9):
            return False
        if player != PLAYER1 and player != PLAYER2:
            return False
            
        # Make move if position has not been played
        if self.board[position] == UNPLAYED:
            self.board[position] = player
            return True
        else:
            return False
    # End Def

    def undo_move(self, position):
        """
        Function undoes the move at paramater position.
        Returns True when a move is actually reversed, otherwise False.
        
        """
        # Bounds Check
        if position not in range(9):
            return False        
        elif self.board[position] != UNPLAYED:
            self.board[position] = UNPLAYED
            return True
        else:
            return False
    # End Def

    def get_valid_moves(self):
        """
        This function returns a list of valid move positions
    
        """
        count = 0
        valid_moves = []
        for current in self.board:
            if current == UNPLAYED:
                valid_moves.append(count)
            count += 1
        return valid_moves
    # End Def
    
    def player_weak_AI_move(self, player):
        """
        This function will make a randomized move for parameter player
        based on the current board state. Returns True if move made,
        otherwise returns False
        
        """
        moves = self.get_valid_moves()
        if moves:
            # Mix up list for random results from AI and Move w/ the top result
            random.shuffle(moves)
            return self.move(moves.pop(), player)
        return False
    # End Def
    
    def player_AI_move(self, player):
        """
        This function will make the best possible move for parameter player
        based on the current board state.
        
        """
        moves = [(move, self.eval_move_wrapper(move, player)) for move in self.get_valid_moves()]
        if moves:
            # Mix up list for less predictable results from AI
            random.shuffle(moves)
            # Line them up worst to best and move with best
            moves.sort(key= lambda (position, outcome): outcome)
            return self.move(moves.pop()[0], player)
        return False
    # End Def    
    
    def opponent(self, player):
        """
        Takes parameter player and returns the opponent player
        
        """
        if player == PLAYER1:
            return PLAYER2
        else:
            return PLAYER1
    # End Def

    def eval_move_wrapper(self, position, player):
        """
        eval_move_wrapper - wrapper function for recursive function
        to determinine best move for paramter player starting with 
        paramter position.
        Returns: worst possible outcome
            (-1 : possible loss)
            (0 : cats game)
            (1 : guaranteed win)
        
        """
        return self.eval_move(position, player, player)
    # End Def
    
    def eval_move(self, position, player, current_player):
        """
        Recursive function for determining best move
        for paramter player starting with paramter position.
        Paramter current_player is the current player to move
        in the simulation.
        Returns: worst possible outcome
            (-1 : possible loss)
            (0 : cats game)
            (1 : guaranteed win)
        
        """
        try:
            # Execute the move
            self.move(position, current_player)
            
            # Evaluate game outcome
            if self.game_over():
                winner_data = self.winner()
                if winner_data:
                    if winner_data[0] == player:
                        return 1 # (1 is desireable)
                    else: return -1 # (-1 must be avoided)
                else:
                    return 0 # Cats game (worth taking)
                    
            # recurse over all valid moves
            outcomes = (self.eval_move(next, player, 
                self.opponent(current_player)) for next in self.get_valid_moves())

            # We want to express the worst case of this move choice
            if player == current_player:
                worst_case = 1
                for outcome in outcomes:
                    if outcome == -1:
                        return -1
                    else:
                        worst_case = min(outcome, worst_case)
                return worst_case
                    
            # We want to express the best case of this move choice
            else:
                best_case = -1
                for outcome in outcomes:
                    if outcome == 1:
                        return 1
                    else:
                        best_case = max(outcome, best_case)
                return best_case
                
        finally: # Undo each move at the tail end of the recursion
            self.undo_move(position)
    # End Def

# End Class Def
