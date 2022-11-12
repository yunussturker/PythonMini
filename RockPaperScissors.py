import random
import time
import sys

print("""Rock, Paper, Scissors by Yunus Emre Türker
- Rock beats scissors.
- Scissors beats paper.
- Paper beats rocks.""")
w = 0
l = 0
d = 0

while True:
    while True:
        print(f'{w} Wins, {l} Lossess {d} Draws.')
        print('Enter your move: (R)ock, (P)aper, (S)cissors or (Q)uit')
        playerMove = input('>>> ').upper()
        if playerMove == 'Q':
            print('Goodbye!')
            sys.exit()
        elif playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Please type one of these. "R / P / S / Q"')

    if playerMove == 'R':
        print('ROCK vs.')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER vs.')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS vs.')
        playerMove = 'SCISSORS'

    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    randNum = random.randint(1, 3)
    if randNum == 1:
        computerMove = 'ROCK'
    elif randNum == 2:
        computerMove = 'PAPER'
    elif randNum == 3:
        computerMove = 'SCISSORS'
    print(computerMove)
    time.sleep(0.5)

    if playerMove == computerMove:
        print("It's a draw!")
        d += 1
    elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
        print("You win!")
        w += 1
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print("You win!")
        w += 1
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print("You win!")
        w += 1
    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print("You lose!")
        l += 1
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print("You lose!")
        l += 1
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print("You lose!")
        l += 1