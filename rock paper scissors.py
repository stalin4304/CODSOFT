import tkinter as tk
import random

player_score = 0
computer_score = 0

def play(player):
    global player_score, computer_score

    computer = random.choice(["Rock", "Paper", "Scissors"])

    player_label.config(text=f"You: {player}")
    computer_label.config(text=f"Computer: {computer}")

    if player == computer:
        result_label.config(text="It's a Tie!")
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        player_score += 1
        result_label.config(text="You Win!")
    else:
        computer_score += 1
        result_label.config(text="Computer Wins!")
    score_label.config(
        text=f"Score: You {player_score} - {computer_score} Computer"
    )

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_label.config(text="You: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Choose a move")
    score_label.config(text="Score: You 0 - 0 Computer")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

title = tk.Label(root, text="Rock Paper Scissors",font=("Arial", 16, "bold"))
title.pack(pady=10)

player_label = tk.Label(root, text="You: ", font=("Arial", 12))
player_label.pack()
computer_label = tk.Label(root, text="Computer: ", font=("Arial", 12))
computer_label.pack()
result_label = tk.Label(root, text="Choose a move", font=("Arial", 14))
result_label.pack(pady=10)
score_label = tk.Label(root,text="Score: You 0 - 0 Computer",font=("Arial", 12, "bold"))
score_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Rock", width=10,command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper",width=10,command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10,command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

tk.Button(root, text="Reset Game",width=15,command=reset_game).pack(pady=10)

root.mainloop()