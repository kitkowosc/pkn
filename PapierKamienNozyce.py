import random

### random comment

# Global variables to keep track of the game state
wins = 0
losses = 0
draws = 0

def playerMove():
    """Handles player input."""
    move = input("Wybierz (k)amień, (p)apier, (n)ożyce lub (w)yjdź: ").lower()
    while move not in ['k', 'p', 'n', 'w']:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        move = input("Wybierz (k)amień, (p)apier, (n)ożyce lub (w)yjdź: ").lower()
    return move

def computerMove():
    """Generates the computer's move."""
    return random.choice(['k', 'p', 'n'])

def game_result(player, computer):
    """Determines the result of the game."""
    global wins, losses, draws
    if player == computer:
        draws += 1
        return "To remis!"
    elif (player == 'k' and computer == 'n') or (player == 'p' and computer == 'k') or (player == 'n' and computer == 'p'):
        wins += 1
        return "Wygrana!"
    else:
        losses += 1
        return "Przegrana!"

def main():
    global wins, losses, draws
    print("Witaj w grze Papier, Kamień, Nożyce!")
    while True:
        player = playerMove()
        if player == 'w':
            break
        computer = computerMove()
        print(f"Komputer wybrał: {computer}")
        result = game_result(player, computer)
        print(result)
        print(f"Wygrane: {wins}, Przegrane: {losses}, Remisy: {draws}")

if __name__ == "__main__":
    main()