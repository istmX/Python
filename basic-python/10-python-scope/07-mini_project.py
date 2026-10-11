# Mini Project: Game Score Tracker
# This project shows how scope works in a small game.

# Global variables: shared across the whole program
player_name = "Aryan"
total_score = 0
games_played = 0


def play_round(points):
    """Play one round and update the global score."""
    global total_score, games_played

    # 'points' is a local variable (a parameter)
    total_score = total_score + points
    games_played = games_played + 1
    print(f"Round finished! You earned {points} points.")


def show_stats():
    """Show current stats. Reads globals, changes nothing."""
    print("-" * 30)
    print(f"Player: {player_name}")
    print(f"Games played: {games_played}")
    print(f"Total score: {total_score}")
    if games_played > 0:
        average = total_score / games_played
        print(f"Average per game: {average:.1f}")
    print("-" * 30)


def reset_game():
    """Reset the score using a nested function to show nonlocal."""
    # This nested function demonstrates that inner functions
    # can read outer function variables.
    message = "Game reset! All scores cleared."

    def print_message():
        # 'message' comes from the enclosing function (outer scope)
        print(message)

    print_message()

    global total_score, games_played
    total_score = 0
    games_played = 0


# ---- Game loop ----
print("Welcome to the Score Tracker!")
print()

play_round(100)
play_round(250)
play_round(75)
show_stats()

print()
reset_game()
show_stats()
