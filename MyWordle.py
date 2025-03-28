import tkinter as tk
from tkinter import messagebox

# Create the main application window
window = tk.Tk()
window.title("Wordle")
window.geometry("400x400")

# Title label
title = tk.Label(
    text="Wordle",
    fg="white",
    bg="gray",
    width=40,
    height=3
)
title.pack()

# Instructions label
instructionsLabel = tk.Label(
    text="Enter a 5-letter word",
    fg="white",
    bg="green"
)
instructionsLabel.pack()

# Input field for user guesses
entry1 = tk.Entry()
entry1.pack()


# Function to handle submissions
def submitGuess():
    secret_word = "apple"               # The word to guess
    guess = entry1.get().lower()        # Get user input and convert to lowercase
    entry1.delete(0, tk.END)            # Clear the input field
    
    # Validate input length
    if len(guess) != 5:
        messagebox.showerror("Error", "Please enter a 5-letter word.")
        return
    
    # Create a frame to display each guess, with letters colored based on correctness
    frame = tk.Frame(master=window)
    
    for i in range(5):
        # Determine color based on correctness of each letter
        if guess[i] == secret_word[i]:
            clueColor = "green"         # Correct letter in correct position
        elif guess[i] in secret_word:
            clueColor = "yellow"        # Correct letter in wrong position
        else:
            clueColor = "gray"          # Incorrect letter
        
        # Display each letter with its corresponding color
        letterLabel = tk.Label(master=frame, text=guess[i], borderwidth=5, relief="sunken", bg=clueColor)
        letterLabel.pack(side="left")
        
        # Check if the guess matches the secret word
        if guess == secret_word:
            messagebox.showinfo("Congratulations", "You guessed the word!")
            window.quit()               # Exit the application
            break
    frame.pack()  # Display the frame to the window
    return


# Submit button to trigger the guess submission
submit_button = tk.Button(text="Submit", command=submitGuess)
submit_button.pack()


# Run the application
window.mainloop()
