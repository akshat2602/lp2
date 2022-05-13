def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print("\n\n")


def isSafe(board, row, col):
    for i in range(N):
        if board[row][i] == 1:
            return False
        if board[i][col] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while j < N and i < N:
        if board[i][j] == 1:

            return False
        i += 1
        j += 1
    return True


def solveNQUtil(board, row):
    if row == N:
        global sol
        printSolution(board)
        print("\n\n")
        sol += 1
        return

    for i in range(N):
        if isSafe(board, row, i):
            board[row][i] = 1
            solveNQUtil(board, row + 1)
            board[row][i] = 0
    return


sol = 0


def solveNQ():
    global N
    N = int(input("Enter number of columns: "))
    board = [[0 for col in range(N)] for row in range(N)]
    while True:
        choice = int(input("\n\nEnter \n1: Using Backtracking\n2: Exit\n\n"))
        if choice == 1:
            solveNQUtil(board, 0)
            print(sol)
        elif choice == 3:
            break
        else:
            print("\nWrong input\n\n")
    return True


solveNQ()