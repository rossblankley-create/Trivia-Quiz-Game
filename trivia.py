# trivia.py
# PY06 – Trivia Quiz Game (Starter)
# ---------------------------------
# You will complete the TriviaGame methods below.
# Follow the step-by-step instructions in the project doc.

import random
import time
from questions import question_bank  # Import the question list

class TriviaGame:
    """
    Organizes game data and behavior.
    You will complete the TODOs in start_game, ask_question, and show_score.
    """

    def __init__(self, questions):
		# Store question bank
        self.question_bank = questions
		# Initialize score
	    self.score = 0

    def start_game(self):
        print("Trivia Game Script Running")
        """
        STEPS 1 & 5:
        - Print a welcome message.
		- Shuffle questions to make it random 
        - Loop through questions (or a subset) and call ask_question() each time.
        - After the loop, call show_score().
        """
        print("Welcome to the World's Coolest Trivia Game!")
		print("Let's see what you know - or don't know!!\n")

	    # Shuffle the questions (just for fun!)
	    random.shuffle(self.question_bank)

	    # Loop through our AMAZING questions!
	    for question in self.question_bank:
			self.ask_question

	    # Now that we're done, Lets see the score

    def ask_question(self, question):
        """
        STEPS 2 & 3:
        - Print the question and options, one per line.
        - Get the user's input with input().
		- Let's omit the timer (this time)
        - Compare their answer (lowercased) to the correct answer.
        - If correct: print confirmation and increment self.score by 1.
        - If incorrect: show the correct answer.
        """
        print(question["question"]:
		for option in question["options"]:
            print(option)
		
        # Here's the timer logic (just in case we change our minds...)
	    # start_time = time.time()
	    # answer = input("Type your choice (a/b/c/d) and press Enter: ")
	    # elapsed = time.time() - start_time

	    # if elapsed > 5:  # As best as I can tell, 5 sec is a completely arbitrary value
	    #     print("Too Late!! No points for this question!\n")
	    # else:
	    #    # Normalize input and compare to correct answer
	    #    if answer.strip().lower() == question["answer"].strip().lower():
	    #        print("Correct!!\n")
	    #    else:
	    #        print("Sorry!! That's NOT correct.")
	    #        print(f"The correct answer was: {question['answer']}\n")
	
    def show_score(self):
        """
        STEP 4:
        - Print a final summary, e.g., "Game Over! You scored X out of Y."
        """
        print("Game Over!")
		print(f"You sscored {self.score} out of {len(self.question_bank)}.")

if __name__ == "__main__":
    game = TriviaGame(question_bank)
    game.start_game()
