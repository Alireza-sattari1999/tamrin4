
import random
from colorama import Fore
import datetime
print("welcome!")
print("tic tac toe!!!")
def see_board():
    for i in range(3):
        for j in range(3):
            if game[i][j] == "X":
                print(Fore.YELLOW + "X", end=" ")
            elif game[i][j] == "O":
                print(Fore.RED + "O", end=" ")
            else:
                print(Fore.BLUE + "-", end=" ")
        print(Fore.RESET)
def check(user, start_time):
    str = game[0][0] + game[1][1] + game[2][2] + " " + game[0][2] + game[1][1] + game[2][0]
    for i in range(3):
        str += " " + game[i][0] + game[i][1] + game[i][2] + " " + game[0][i] + game[1][i] + game[2][i]
    if "OOO" in str:
            print("avali bord")
            print("zaman bazi: ", datetime.datetime.now() - starting_time)
            exit()
    elif "XXX" in str:
            if user == "p2":
                print("dovomi bord.")
            else:
                print("pc bord")
            print("zaman bazi:", datetime.datetime.now() - starting_time)
            exit()
def bazi_ba_dovomi(starting_time):
    Number_of_game_moves = 9
    while True:
        while True:
            row = int(input(" enter row: "))
            col = int(input(" enter col: "))
            if row in range(0, 3) and col in range(0, 3):
                if game[row][col] == "-":
                    game[row][col] = "O"
                    break
                else:
                    print("in khone khali nist")
            else:
                print("error")
        see_board()
        check("p2", starting_time)
        if Number_of_game_moves == 1:
        
            print("tie!!!")
            print("zaman bazi: ", datetime.datetime.now() - starting_time)
            break
        Number_of_game_moves -= 2

        while True:
            row = int(input(" enter row: "))
            col = int(input(" enter col: "))
            if row in range(0, 3) and col in range(0, 3):
                if game[row][col] == "-":
                    game[row][col] = "X"
                    break
                else:
                    print("error")
            else:
                print("error ")
        
        see_board()
        check("p2", starting_time)
def bazi_ba_computer(starting_time):
    Number_of_game_moves = 9
    while True:
        while True:
            row = int(input(" enter row: "))
            col = int(input(" enter col: "))
            if row in range(0, 3) and col in range(0, 3):
                if game[row][col] == "-":
                    game[row][col] = "O"
                    break
                else:
                    print("khone khali nist")
        else:
                 print("error!")
        see_board()
        check("computer", starting_time)
        print("-----------------")
        if Number_of_game_moves == 1:
            print("Tie!!!")
            print("zaman bazi ", datetime.datetime.now() - starting_time)
            break
        Number_of_game_moves -= 2
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if row in range(0, 3) and col in range(0, 3):
                if game[row][col] == "-":
                    game[row][col] = "X"
                    break
            see_board()
            check("pc", starting_time)
game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]
see_board()
n = input("baraye bazi ba dovomi 2 va baraye bazi ba computer 1 ra vared konid: ")
if n == "1":
    starting_time = datetime.datetime.now()
bazi_ba_computer(starting_time) 
if n == "2":
    starting_time = datetime.datetime.now()
    bazi_ba_dovomi(starting_time)