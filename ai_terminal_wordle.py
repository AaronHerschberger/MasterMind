import random
import tkinter as tk
from tkinter import messagebox

# Initial Commit Version

def load_words():
    return ["apple", "grape", "peach", "berry", "mango"]

def get_feedback(secret_word, guess):
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append("G")  # Correct letter and position
        elif guess[i] in secret_word:
            feedback.append("Y")  # Correct letter, wrong position
        else:
            feedback.append("B")  # Incorrect letter
    return "".join(feedback)

class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle")
        self.words = load_words()
        self.secret_word = random.choice(self.words)
        self.attempts = 6
        self.current_attempt = 0

        self.label = tk.Label(root, text="Guess the 5-letter word. Feedback: G=Green, Y=Yellow, B=Black")
        self.label.pack()

        self.guesses_frame = tk.Frame(root)
        self.guesses_frame.pack()
        self.guesses = []

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_guess)
        self.submit_button.pack()

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

    def submit_guess(self):
        guess = self.entry.get().lower()
        if len(guess) != 5:
            messagebox.showerror("Error", "Please enter a 5-letter word.")
            return

        feedback = get_feedback(self.secret_word, guess)
        self.feedback_label.config(text=f"Feedback: {feedback}")
        self.current_attempt += 1

        if guess == self.secret_word:
            messagebox.showinfo("Congratulations", "You guessed the word!")
            self.root.quit()
        elif self.current_attempt >= self.attempts:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The word was: {self.secret_word}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()