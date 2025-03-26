import tkinter as tk
from tkinter import messagebox

# Initial Commit Version

window = tk.Tk()
window.title("Wordle")
window.geometry("400x400")

title = tk.Label(
    text="Wordle",
    fg="white",
    bg="gray",
    width=40,
    height=3
)
title.pack()

instructionsLabel = tk.Label(
    text="Enter a 5-letter word",
    fg="white",
    bg="green"
)
instructionsLabel.pack()

entry1 = tk.Entry()
entry1.pack()



def submitGuess():
    secret_word = "apple"
    guess = entry1.get().lower()
    entry1.delete(0, tk.END)
    
    if len(guess) != 5:
        messagebox.showerror("Error", "Please enter a 5-letter word.")
        return
    
    frame = tk.Frame(master=window)
    for i in range(5):
        if guess[i] == secret_word[i]:
            clueColor = "green"
        elif guess[i] in secret_word:
            clueColor = "yellow"
        else:
            clueColor = "gray"
        
        letterLabel = tk.Label(master=frame, text=guess[i], borderwidth=5, relief="sunken", bg=clueColor)
        letterLabel.pack(side="left")
        
        if guess == secret_word:
            messagebox.showinfo("Congratulations", "You guessed the word!")
            window.quit()
            break
    frame.pack()
    return


submit_button = tk.Button(text="Submit", command=submitGuess)
submit_button.pack()


window.mainloop()


