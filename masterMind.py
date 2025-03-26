import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("MasterMind")
window.geometry("400x400")

title = tk.Label(
    text="MasterMind",
    fg="white",
    bg="blue",
    width=40,
    height=3
)
title.pack()

instructionsLabel = tk.Label(
    text="Enter any 4-digit sequence",
    fg="white",
    bg="purple"
)
instructionsLabel.pack()

entry1 = tk.Entry(width=22)
entry1.pack()

secret_sequence = "2345"



def submitGuess():
    guess = entry1.get()
    entry1.delete(0, tk.END)
    
    if len(guess) != 4:
        messagebox.showerror("Error", "Please enter a 4-number sequence.")
        return
    
    frame = tk.Frame(master=window)
    for i in range(4):
        if guess[i] == secret_sequence[i]:
            clueColor = "green"
        elif guess[i] in secret_sequence:
            clueColor = "yellow"
        else:
            clueColor = "gray"
        
        letterLabel = tk.Label(master=frame, text=guess[i], borderwidth=5, relief="sunken", bg=clueColor)
        letterLabel.pack(side="left")
        
    if guess == secret_sequence:
        messagebox.showinfo("Congratulations", "You guessed the sequence!")
        entry1.insert(0, "The sequence was: " + secret_sequence)
    
    frame.pack()
    return


submit_button = tk.Button(text="Submit", command=submitGuess)
submit_button.pack()


window.mainloop()


