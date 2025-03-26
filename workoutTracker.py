import tkinter as tk
from tkinter import messagebox

# Initial Commit Version


## Data types
# Workout data type
class exercise:
    def __init__(self, name, sets, reps, weight):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} - {self.sets} x {self.reps} @ {self.weight} lbs"
    

# Workout data type
class workout:
    def __init__(self, name, exercises: list[exercise]):
        self.name = name
        self.exercises = exercises
    
    def __str__(self):
        return f"{self.name} - {self.exercises}"


# Create default instance of workout
defaultExercises = [
    exercise("Squats", 3, 10, 135),
    exercise("Bench Press", 3, 10, 135),
    exercise("Deadlift", 3, 10, 135)
]

defaultWorkout = workout("Workout A", defaultExercises)



def on_checkbox_toggle():
    if checkbox_var.get():
        messagebox.showinfo("Checkbox", "Congrats! You finished the workout!")
    else:
        messagebox.showinfo("Checkbox", "Settings reset")


# Create the root window
root = tk.Tk()
root.title("Workout Tracker")

# Create labels for sections
labelA = tk.Label(root, text="Step A")
labelA.pack()
# Display mini checkboxes for default exercises
# Create a checkbox for each exercise
for ex in defaultExercises:
    cb = tk.Checkbutton(root, text=ex.name, variable=False, command=on_checkbox_toggle)
    cb.pack()

labelB = tk.Label(root, text="Step B")
labelB.pack()


checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Check me", variable=checkbox_var, command=on_checkbox_toggle)

checkbox.pack(pady=200)

root.mainloop()