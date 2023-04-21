import random

square_game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def view_table():
    first_line = " | "
    for element in square_game[0]:
        first_line += element + " | "

    second_line = " | "
    for element in square_game[1]:
        second_line += element + " | "

    third_line = " | "
    for element in square_game[2]:
        third_line += element + " | "

    print(first_line)
    print(second_line)
    print(third_line)


def test_positions(num):
    if 0 <= num <= 2:
        return True
    return False


def ask_positions():
    row = int(input("Escoge una fila entre 0 y 2 = "))
    while not test_positions(row):
        row = int(input("Escoge una fila entre 0 y 2 = "))

    column = int(input("Escoge una columna entre 0 y 2 = "))
    while not test_positions(column):
        column = int(input("Escoge una columna entre 0 y 2 = "))

    return [row, column]


def test_rules(coord_row, coord_column):
    content = square_game[coord_row][coord_column]
    if not content == " ":
        return False
    return True


def view_winner(pyr):
    win1 = square_game[0][0] == pyr and square_game[0][1] == pyr and square_game[0][2] == pyr
    win2 = square_game[1][0] == pyr and square_game[1][1] == pyr and square_game[1][2] == pyr
    win3 = square_game[2][0] == pyr and square_game[2][1] == pyr and square_game[2][2] == pyr
    win4 = square_game[0][0] == pyr and square_game[1][0] == pyr and square_game[2][0] == pyr
    win5 = square_game[0][1] == pyr and square_game[1][1] == pyr and square_game[2][1] == pyr
    win6 = square_game[0][2] == pyr and square_game[1][2] == pyr and square_game[2][2] == pyr
    win7 = square_game[0][0] == pyr and square_game[1][1] == pyr and square_game[2][2] == pyr
    win8 = square_game[0][2] == pyr and square_game[1][1] == pyr and square_game[2][0] == pyr

    return any([win1, win2, win3, win4, win5, win6, win7, win8])


def game():
    turno = random.randint(0, 1)
    end_game = 0

    while end_game == 0:
        view_table()
        if turno == 1:
            print("le toca al jugador X")

            positions = ask_positions()

            while not test_rules(positions[0], positions[1]):
                positions = ask_positions()

            square_game[positions[0]][positions[1]] = "X"
            if view_winner("X"):
                end_game = 1
            turno = 0

        else:
            print("le toca al jugador O")

            positions = ask_positions()

            while not test_rules(positions[0], positions[1]):
                positions = ask_positions()

            square_game[positions[0]][positions[1]] = "O"
            if view_winner("O"):
                end_game = 1
            turno = 1

        print("------------------------------------")
    winner = ""
    if turno == 1:
        winner = "O"
    else:
        winner = "X"
    print("FELICITACIONES GANA EL JUGADOR " + winner)
    view_table()


game()
