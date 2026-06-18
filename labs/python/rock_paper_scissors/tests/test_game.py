# Tests for the Rock Paper Scissors game
import unittest
from game import Scorer, determine_winner

# Test class for the Scorer class
class TestGame(unittest.TestCase):
    
    # test the determine_winner function
    def test_determine_winner(self):
        self.assertEqual(determine_winner("rock", "scissors"), "player1")
        self.assertEqual(determine_winner("paper", "rock"), "player1")
        self.assertEqual(determine_winner("scissors", "paper"), "player1")
        self.assertEqual(determine_winner("rock", "paper"), "player2")
        self.assertEqual(determine_winner("paper", "scissors"), "player2")
        self.assertEqual(determine_winner("scissors", "rock"), "player2")
        self.assertEqual(determine_winner("rock", "rock"), "tie")
        self.assertEqual(determine_winner("paper", "paper"), "tie")
        self.assertEqual(determine_winner("scissors", "scissors"), "tie")
    
    # used inline GHCP chat with the following prompt:
    # Generated with Copilot: Write test cases for the Scorer class to verify point calculation and score updates.
    def test_calculate_points(self):
        scorer = Scorer()
        self.assertEqual(scorer.calculate_points("rock"), 1)
        self.assertEqual(scorer.calculate_points("paper"), 2)
        self.assertEqual(scorer.calculate_points("scissors"), 3)
        self.assertEqual(scorer.calculate_points("invalid"), 0)

    def test_update_score_player1(self):
        scorer = Scorer()
        scorer.update_score("player1", "rock")
        self.assertEqual(scorer.player1_score, 1)
        self.assertEqual(scorer.player2_score, 0)
        scorer.update_score("player1", "paper")
        self.assertEqual(scorer.player1_score, 3)
        self.assertEqual(scorer.player2_score, 0)

    def test_update_score_player2(self):
        scorer = Scorer()
        scorer.update_score("player2", "scissors")
        self.assertEqual(scorer.player1_score, 0)
        self.assertEqual(scorer.player2_score, 3)
        scorer.update_score("player2", "rock")
        self.assertEqual(scorer.player1_score, 0)
        self.assertEqual(scorer.player2_score, 4)

    def test_update_score_invalid(self):
        scorer = Scorer()
        scorer.update_score("invalid", "rock")
        self.assertEqual(scorer.player1_score, 0)
        self.assertEqual(scorer.player2_score, 0)

    def test_get_final_scores(self):
        scorer = Scorer()
        scorer.update_score("player1", "rock")
        scorer.update_score("player2", "paper")
        self.assertEqual(scorer.get_final_scores(), (1, 2))

    def test_get_winner(self):
        scorer = Scorer()
        scorer.update_score("player1", "rock")  # 1
        scorer.update_score("player2", "paper") # 2
        self.assertEqual(scorer.get_winner(), "Player 2 wins!")
        scorer.update_score("player1", "scissors") # +3, total 4
        self.assertEqual(scorer.get_winner(), "Player 1 wins!")
        scorer = Scorer()
        self.assertEqual(scorer.get_winner(), "It's a tie!")

# main function to run the tests
if __name__ == '__main__':
    unittest.main()