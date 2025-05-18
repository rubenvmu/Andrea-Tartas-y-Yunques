import os

scoreboard_path = "scoreboard.txt"

def save_score(username, score):
    with open(scoreboard_path, "a") as file:
        file.write(f"{username}:{score}\n")

def load_scoreboard():
    if not os.path.exists(scoreboard_path):
        return []
    with open(scoreboard_path, "r") as file:
        entries = []
        for line in file:
            if ":" in line:
                name, score = line.strip().split(":")
                try:
                    entries.append((name, int(score)))
                except ValueError:
                    continue
        return sorted(entries, key=lambda x: x[1], reverse=True)