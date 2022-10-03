a = ""
b = ""
c = ""
d = ""
e = ""
f = ""
x = ""
y = ""
z = ""


game_is_over = False

end_game_massage = ""

def board():
    first_row = f"\n {a} | {b} | {c}  " + "\n _ _ _ _ _\n"
    second_row = f"\n {d} | {e} | {f}  " + "\n _ _ _ _ _\n"
    third_row = f"\n {x} | {y} | {z} " + "\n _ _ _ _ _\n" 
    return first_row + second_row + third_row
    
print(board())

while game_is_over == False:
    
    
    user1 = int(input("First player (X) enter a square number to make it X: " ))

    valid = False
    while valid == False:
        if user1 == 1 and a== "":
            a = "X"
            valid = True
        elif user1 == 2 and b == "":
            b = "X"
            valid = True
        elif user1 == 3 and c =="":
            c= "X"
            valid = True
        elif user1 == 4 and d == "":
            d = "X"
            valid = True
        elif user1 == 5 and e == "":
            e = "X"
            valid = True
        elif user1 == 6 and f == "":
            f = "X"
            valid = True
        elif user1 == 7 and x == "":
            x = "X"
            valid = True
        elif user1 == 8 and y == "":
            y = "X"
            valid = True
        elif user1 == 9 and z == "":
            z = "X"
            valid = True
        else:
            print("Invalid move please repeat")
    

    print(board())
    

    user2 = int(input("Second player (O) enter a square number to make it O: " ))
    valid = False
    while valid == False:
        if user2 == 1 and a == "":
            a = "O"
            valid = True
        elif user2 == 2 and b == "":
            b = "O"
            valid = True
        elif user2 == 3 and c =="":
            c= "O"
            valid = True
        elif user2 == 4 and d == "":
            d = "O"
            valid = True
        elif user2 == 5 and e == "":
            e = "O"
            valid = True
        elif user2 == 6 and f == "":
            f = "O"
            valid = True
        elif user2 == 7 and x == "":
            x = "O"
            valid = True
        elif user2 == 8 and y == "":
            y = "O"
            valid = True
        elif user2 == 9 and z == "":
            z = "O"
            valid = True
        else:
            print("Invalid move please repeat")
    
    print(board())
    
    if a == b == c == "X" or d == e == f == "X" or x == y == z == "X" :
        game_is_over = True
        end_game_massage = "First player (X) has won."
    
    elif a == b == c == "O" or d == e == f == "O" or x == y == z == "O":
        game_is_over = True
        end_game_massage = "second player (O) has won."


    elif a == d == x == "X" or b == e == y == "X" or c == f == z == "X" :
        game_is_over = True
        end_game_massage = "First player (X) has won."
    
    elif a == d == x == "O" or b == e == y == "O" or c == f == z == "O":
        game_is_over = True
        end_game_massage = "second player (O) has won."

    elif a == e == z == "X" or c == e == x == "X":
        game_is_over = True
        end_game_massage = "First player (X) has won."
    
    elif a == e == z == "O" or c == e == x == "O":
        game_is_over = True
        end_game_massage = "second player (O) has won."

    elif a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and x != "" and y != "" and z != "":
        game_is_over = True
        end_game_massage = "Draw!"


print(board())
print(end_game_massage)
