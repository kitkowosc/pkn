import random, sys
print("Papier, Kamień, Nożyce")
# zmienne do przechowywania ilości zwycięstw, porażek, remisów
wins = 0
losses = 0
draws = 0

while True: #pętla główna gry
    print('%s zwycięstw, %s porażek, %s remisów' %(wins, losses, draws))
    while True: #pętla danych wejściowych gracza
        print("Podaj swój wybór: (k)amień, (p)apier, (n)ożyce lub (w)yjście")
        playerMove = input()
        if playerMove == "w":
            sys.exit() #zakończenie działania programu
        if playerMove == "k" or playerMove == "p" or playerMove == "n":
            break #opuszczenie pętli danych wejściowych gracza
        print("Wpisz literę k, p, n lub w.")
    #wyświetlanie wyboru dokonanego przez gracza
    if playerMove == "k":
        print("Kamień vs ....")
    elif playerMove == "p":
        print("Papier vs ....")
    elif playerMove == "n":
        print("Nożyce vs ....")

    #wyświetlanie wyboru dokonanego przez komputer
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = "k"
        print("Kamień")
    elif randomNumber == 2:
        computerMove = "p"
        print("Papier")
    elif randomNumber == 3:
        computerMove = "n"
        print("Nożyce")
    #wyświetlanie i rejestrowanie stanu gry

    if playerMove == computerMove:
        print("To remis!")
        draws = draws + 1
    elif playerMove == "k" and computerMove == "n":
        print("Wygrana!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "k":
        print("Wygrana!")
        wins = wins + 1
    elif playerMove == "n" and computerMove == "p":
        print("Wygrana!")
        wins = wins + 1
    else:
        print("Wygrywa komputer!")
        losses = losses + 1