"""Rock, paper, scissors against the computer, best of any number of rounds."""

import random

MOVES = {"r": "rock", "p": "paper", "s": "scissors"}
BEATS = {"r": "s", "p": "r", "s": "p"}  # each move beats the one it maps to


def winner(player: str, computer: str) -> str:
    if player == computer:
        return "tie"
    return "player" if BEATS[player] == computer else "computer"


def main() -> None:
    score = {"player": 0, "computer": 0, "tie": 0}
    print("Rock, paper, scissors. Type r, p or s, or q to quit.")
    while True:
        choice = input("\nYour move: ").strip().lower()[:1]
        if choice == "q":
            break
        if choice not in MOVES:
            print("Type r, p, s or q.")
            continue
        computer = random.choice(list(MOVES))
        result = winner(choice, computer)
        score[result] += 1
        print(f"You: {MOVES[choice]}   Computer: {MOVES[computer]}")
        print({"tie": "Tie.", "player": "You win this round.", "computer": "Computer wins this round."}[result])
        print(f"Score  you {score['player']} : {score['computer']} computer  ({score['tie']} ties)")
    print(f"\nFinal score: you {score['player']}, computer {score['computer']}, ties {score['tie']}.")


if __name__ == "__main__":
    main()
