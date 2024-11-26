import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x500")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissor"]

player_score = 0
computer_score = 0

def play(choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    result = ""
    if choice == computer_choice:
        result = "It's a Draw!"
    elif (choice == "Rock" and computer_choice == "Scissor") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissor" and computer_choice == "Paper"):
        player_score += 1
        result = "You Win!"
    else:
        computer_score += 1
        result = "Computer Wins!"

    result_label.config(text=f"Result: {result}")
    player_score_label.config(text=f"Your Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    computer_choice_label.config(text=f"Computer Chose: {computer_choice}")

def reset_game():
    global player_score, computer_score
    player_score, computer_score = 0, 0
    result_label.config(text="Result:")
    player_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    computer_choice_label.config(text="Computer Chose: None")


def exit_game():
    if messagebox.askyesno("Exit Game", "Are you sure you want to exit?"):
        root.destroy()


title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

player_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 14))
player_score_label.pack()

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 14))
computer_score_label.pack()

computer_choice_label = tk.Label(root, text="Computer Chose: None", font=("Arial", 14))
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Result:", font=("Arial", 16, "bold"), fg="blue")
result_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissor_button = tk.Button(button_frame, text="Scissor", font=("Arial", 14), width=10, command=lambda: play("Scissor"))
scissor_button.grid(row=0, column=2, padx=10)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), width=15, bg="orange", command=reset_game)
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit Game", font=("Arial", 14), width=15, bg="red", command=exit_game)
exit_button.pack(pady=10)
root.mainloop()
