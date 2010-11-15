"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from tic_tac_toe.game import TicTacToe

class TicTacToeTest(TestCase):
    """
    This is the test cases for TicTacToe project
    
    """
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        
        """
        self.failUnlessEqual(1 + 1, 2)
    # End Def    
    
    def test_tic_tac_toe_game(self):
        """
        Tests the base functionality of the tic_tac_toe game.py file
        functions covered: get_constants, new_game, get_valid_moves, move, 
        undo_move, player_AI_move, player_weak_AI_move and consequently opponent,
        eval_move_wrapper, and eval_move.
        
        """
        # create our name
        game = TicTacToe()
        unplayed, player1, player2 = game.get_constants()
        
        # Make a series of moves, test get_valid_moves along the way
        game.move(0, player1)
        self.assertEqual(game.get_valid_moves(), range(1,9))
        game.move(8, player2)
        self.assertEqual(game.get_valid_moves(), range(1,8))
        game.move(1, player1)
        self.assertEqual(game.get_valid_moves(), range(2,8))
        game.move(3, player2)
        self.assertEqual(game.get_valid_moves(), [2, 4, 5, 6, 7])
        game.move(2, player1)
        self.assertEqual(game.get_valid_moves(), range(4,8))
        game.move(4, player2)
        self.assertEqual(game.get_valid_moves(), range(5,8))
        game.move(6, player1)
        self.assertEqual(game.get_valid_moves(), [5,7])
        
        # In the previous series of moves player 1 won w/ [0, 1, 2].
        self.assertTrue(game.game_over())
        self.assertEqual(game.winner(), [player1, [0, 1, 2]])
        
        # Ok, now lets test winner for all cases
        winners = [    [0,1,2],[3,4,5],[6,7,8],    # verticals
                       [0,3,6],[1,4,7],[2,5,8],    # horizontals
                       [0,4,8],[2,4,6] ]           # diagonals
        for winner in winners:
            game.new_game()
            for position in winner:
                game.move(position, player1)
            self.assertEqual(game.winner(), [player1, winner])
        game.new_game()
        
        # Test undo_move
        game.move(0, player1)
        game.undo_move(0)
        self.assertEqual(game.get_valid_moves(), range(9))
        self.assertEqual(game.undo_move(0), False)
        self.assertEqual(game.undo_move(10), False)
        
        # Set player_AI_move against player_weak_AI_move 
        # and verify weak_AI never wins even when going first
        for occurance in range(25):
            print "Testing game " + str(occurance)
            game.new_game()
            self.assertEqual(game.get_valid_moves(), range(9))
            current_player = player2
            while not game.game_over():
                if current_player == player2:
                    game.player_AI_move(player2)
                    current_player = player1
                elif current_player == player1:
                    game.player_weak_AI_move(player1)
                    current_player = player2
            self.assertTrue(game.game_over())
            winner_data = game.winner()
            if winner_data:
                self.assertEqual(winner_data[0], player2)
    # End Def
        
if __name__ == '__main__':
    unittest.main()
