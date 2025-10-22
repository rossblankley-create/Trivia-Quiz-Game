# trivia.py
# PY06 – Trivia Quiz Game (Starter)
# ---------------------------------
# You will complete the TriviaGame methods below.
# Follow the step-by-step instructions in the project doc.

import random
from questions import question_bank  # Import the question list

class TriviaGame:
    """
    Organizes game data and behavior.
    You will complete the TODOs in start_game, ask_question, and show_score.
    """

    def __init__(self, questions):
        pass

    def start_game(self):
        """
        STEP 1:
        - Print a welcome message.
        - Loop through questions (or a subset) and call ask_question() each time.
        - After the loop, call show_score().
        """
        """
        STEP 5:
	        - Use random.shuffle() on question_bank before the for loop to randomize.
        """

        pass


    def ask_question(self, question):
        """
        STEP 2 & 3:
        - Print the question and options, one per line.
        - Get the user's input with input().
        - Compare their answer (lowercased) to the correct answer.
        - If correct: print confirmation and increment self.score by 1.
        - If incorrect: show the correct answer.
        """
        pass  # TODO: Implement the logic described above.

    def show_score(self):
        """
        STEP 4:
        - Print a final summary, e.g., "Game Over! You scored X out of Y."
        """
        pass  # TODO: Implement final score display.


if __name__ == "__main__":
    game = TriviaGame(question_bank)
    game.start_game()