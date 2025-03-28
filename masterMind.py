import tkinter as tk
from tkinter import messagebox
import random

# Create main window
window = tk.Tk()
window.title("MasterMind")
window.geometry("400x600")

# Title label
title = tk.Label(
    font=("Arial", 20, "italic bold"),
    text="MasterMind",
    fg="white",
    bg="blue",
    height=3
)
title.pack(fill=tk.X)

# Instructions label
instructionsLabel = tk.Label(
    font=("Arial", 12),
    text="Enter any 4-digit sequence",
    fg="white",
    bg="purple"
)
instructionsLabel.pack(padx=10, pady=10)

# Input entry field
entry1 = tk.Entry(width=22)
entry1.pack()

# Secret sequence to guess
secret_sequence = "1776"                            # Predefined sequence for testing
# Uncomment the following line to generate a random sequence
secret_sequence = str(random.randint(0, 9999)).zfill(4) # Generate a random 4-digit number, padded with zeros


# Function to handle guess submission
def submitGuess():
    guess = entry1.get()                          # Get user input
    entry1.delete(0, tk.END)                      # Clear input field
    
    if len(guess) != 4:                           # Validate length
        messagebox.showerror("Error", "Please enter a 4-number sequence.")
        return
    if not guess.isdigit():                       # Validate numeric input
        messagebox.showerror("Error", "Please enter only numbers.")
        return
    
    frame = tk.Frame(master=window)               # Create frame for guess feedback
    for i in range(4):                            # Check each digit
        if guess[i] == secret_sequence[i]:        # Correct digit and position
            clueColor = "green"
        elif guess[i] in secret_sequence:         # Correct digit, wrong position
            clueColor = "yellow"
        else:                                     # Incorrect digit
            clueColor = "gray"
        
        # Display each digit, colored based on correctness
        letterLabel = tk.Label(master=frame, text=guess[i], borderwidth=5, relief="sunken", bg=clueColor, width=2)
        letterLabel.pack(side="left", padx=5, pady=5)
        
    if guess == secret_sequence:                  # Check if guess is correct
        messagebox.showinfo("Congratulations", "You guessed the sequence!")
        entry1.insert(0, "The sequence was: " + secret_sequence)
        entry1.config(state="disabled")           # Disable input field
        submit_button.config(state="disabled")    # Disable submit button
    
    frame.pack()                                  # Display feedback frame
    return

# Submit button
submit_button = tk.Button(text="Submit", command=submitGuess)
submit_button.pack(padx=10, pady=10)

# Run the application
window.mainloop()
