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
    if num <= 2 and num >= 0:
        return True
    return False


def game():
    turno = random.randint(0, 1)
    end_game = 0
    print(turno)

    while end_game == 0:
        view_table()
        if turno == 1:
            print("le toca al jugador X")
            row = input("Escoge una fila entre 0 y 2 = ")
            column = input("Escoge una columna entre 0 y 2 = ")
            if not (test_positions(row) and test_positions(column)):
                print("pwaodapwopo")
            square_game[int(row)][int(column)] = "X"
            turno = 0
        else:
            print("le toca al jugador O")
            row = input("Escoge una fila entre 0 y 2 = ")
            column = input("Escoge una columna entre 0 y 2 = ")
            # square_game[row][column] = "O"
            square_game[int(row)][int(column)] = "O"
            turno = 1


game()
