from tkinter import Tk, Button, Label, StringVar
import random

# List of choices
choices = ["Rock", "Paper", "Scissor"]

# Initialize the main window
window = Tk()
window.geometry("400x400")
window.title("Rock, Paper, and Scissors")

# Variable to store the player's choice
choice = StringVar()


# Function to decide the result
def decide(player_choice):
    computer_choice = random.choice(choices)  # Randomly select for the computer
    if player_choice == computer_choice:
        msg = f"It's a Tie! Computer chose {computer_choice}."
    elif (player_choice == "Rock" and computer_choice == "Scissor") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissor" and computer_choice == "Paper"):
        msg = f"You Win! Computer chose {computer_choice}."
    else:
        msg = f"You Lose! Computer chose {computer_choice}."

    # Display the result
    result_label.config(text=msg)


# Add buttons for each choice
Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=20)

Button(window, text="Rock", width=20, command=lambda: decide("Rock")).pack(pady=10)
Button(window, text="Paper", width=20, command=lambda: decide("Paper")).pack(pady=10)
Button(window, text="Scissor", width=20, command=lambda: decide("Scissor")).pack(pady=10)

# Label to display the result
result_label = Label(window, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
