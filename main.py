from NQueens import NQueens
import pickle
from functions import breakline, clrscr, take_input
import random
import os

fName = "outputs.pkl"


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j]:
                print('-', end=" ")
            else:
                print('Q', end=" ")
        print()


def gen():
    print('Generating The Outputs to 20 queen problem')
    breakline()
    print('Press ctrl+c To stop generating and save the solutions to a file.')
    breakline()
    input('Press Enter To Begin.')
    breakline()
    try:
        S = NQueens(20).solve()
    except KeyboardInterrupt:
        print('Saving The Generated Outputs!')
    breakline()
    print(f'Saving The Output in {fName}')
    print(len(S))
    pickle.dump(S, open(fName, 'wb'))
    breakline()
    print('Saved!')
    breakline()
    print('A Solution From The saved ones is:')
    print_board(random.choice(list(S.values())))
    breakline()


def prev():
    print('Loading the previously saved outputs!')
    if not os.path.isfile(fName):
        print('No previously saved outputs exist! Generating Them!')
        gen()
    solutions = pickle.load(open(fName, 'rb'))
    N = len(solutions)
    N = random.randint(1, N)
    print_board(solutions[N])


def main():
    breakline()
    print('WELCOME TO 20 QUEENS PROBLEM!')
    take_input(['Generate Outputs', 'Print Previously Generated Ones'], gen, prev)


if __name__ == '__main__':
    main()
