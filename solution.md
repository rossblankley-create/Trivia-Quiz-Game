# Solution Code - Trivia Quiz Game


<details>
<summary>Step 1 Solution – Set Up the Game Structure</summary>

Python - trivia.py

```python
class TriviaGame:
    def __init__(self, questions):
        # STEP 1: Set up starting data
        self.question_bank = questions
        self.score = 0

    def start_game(self):
        """
        STEP 1:
        - Print a welcome message.
        - Loop through questions (or a subset) and call ask_question() each time.
        - After the loop, call show_score().
        """
        print("Welcome to the Python Trivia Game!")

        for question in self.question_bank:
            self.ask_question(question)

```
</details>  


<details>
<summary>Step 2 Solution – Ask a Question</summary>
Python - trivia.py

```python
def ask_question(self, question):
    """
    STEP 2 & 3:
    - Select a random question: random.choice(self.question_bank)
    - Print the question and options, one per line.
    - Get the user's input with input().
    - Compare their answer (lowercased) to the correct answer.
    - If correct: print confirmation and increment self.score by 1.
    - If incorrect: show the correct answer.
    """
    # STEP 2: Display question and collect answer
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Type in your choice (a/b/c/d) and hit Enter: ")

    # STEP 3 logic will be added next
```
</details>   


<details>
<summary> Step 3 Solution – Check the Player’s Answer</summary>
Python - trivia.py

```python
    # STEP 3: Check if the answer is correct
    if answer == question["answer"]:
        print("Correct!")
        self.score += 1
    else:
        print("Sorry, that's not correct.")
        print(f"The correct answer was: {question['answer']}")

    # Show the running score after each question
    print(f"Current score: {self.score}")
```
</details>   


<details>
<summary> Step 4 Solution – Show the Final Score</summary>
Python - trivia.py

```python
def show_score(self):
    """
    STEP 4:
    - Print a final summary, e.g., "Game Over! You scored X out of Y."
    """
    print(f"Game Over! You scored {self.score} out of {len(self.question_bank)}.")

# make sure to add a function call at the bottom of `self.start_game()` method
```
</details>   


<details>
<summary> Step 5 Solution – Randomize the Quiz</summary>
Python - trivia.py

```python
def start_game(self):
    print("Welcome to the Python Trivia Game!")

    # STEP 5: Optional shuffle for randomness
    random.shuffle(self.question_bank)

    for question in self.question_bank:
        self.ask_question(question)

    self.show_score()

```
</details>   


<details>
<summary>Final Solution</summary>
Python - trivia.py

```python
# trivia.py
# PY06 – Trivia Quiz Game (Solution)
# ---------------------------------
# This is the completed version of the TriviaGame class.

import random
import time
from questions import question_bank  # Import the question list

class TriviaGame:
    """
    Organizes game data and behavior.
    """

    def __init__(self, questions):
        # Store the question bank
        self.question_bank = questions
        # Initialize the score
        self.score = 0

    def start_game(self):
        """
        STEP 1 & 5:
        - Print a welcome message.
        - Shuffle questions so the order is random.
        - Loop through each question and call ask_question().
        - After the loop, call show_score().
        """
        print("🎉 Welcome to the Python Trivia Game! 🎉")
        print("Get ready to test your knowledge.\n")

        # Shuffle the questions for variety
        random.shuffle(self.question_bank)

        for question in self.question_bank:
            self.ask_question(question)

        # After all questions, show the final score
        self.show_score()

    def ask_question(self, question):
        """
        STEP 2 & 3:
        - Display the question and options.
        - Get the user's input with input().
        - Check how long they took (optional timer).
        - Compare their answer to the correct one.
        - Give feedback and update the score.
        """
        print(question["question"])
        for option in question["options"]:
            print(option)

        # Optional timer logic
        start_time = time.time()
        answer = input("Type your choice (a/b/c/d) and press Enter: ")
        elapsed = time.time() - start_time

        if elapsed > 5:
            print("⏰ Too late! No points for this question.\n")
        else:
            # Normalize input and compare to correct answer
            if answer.strip().lower() == question["answer"].strip().lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print("❌ Sorry, that’s not correct.")
                print(f"The correct answer was: {question['answer']}\n")

    def show_score(self):
        """
        STEP 4:
        - Print a final summary.
        """
        print("Game Over!")
        print(f"You scored {self.score} out of {len(self.question_bank)}.")

if __name__ == "__main__":
    game = TriviaGame(question_bank)
    game.start_game()
```
</details>