import time

def display(A, B):
    R = A * 2 - 1
    N = -1
    K = 0
    G = A-1
    for i in range(R):
        K = K - (i > R / 2)
        JL = (i + K * 2) * 2 + 1
        for j in range(G):
            print(chr(32),end=" ")
        if (i < R //2): #here
            G = G - 1
        else:
            G = G + 1
        for j in range(JL):
            N = N +1
            if (j == 0) or (j == JL - 1):
                B[N] = 35
            print(chr(B[N]),end=" ")
        print()


def move(A, B, C):
    R = A * 2 - 1
    N = -1
    K = 0
    for i in range(R):
        K = K - (i > R / 2)
        JL = (i + K * 2) * 2 + 1
        for j in range(JL):
            N = N + 1
            if (N == B):
                U = JL - 1 + 2 * (K < 0)
                D = JL + 1 - 2 * (K < 0) - 2 * (JL == 2 * A - 1)
    if (C == "U"):
        B = B - U
    if (C == "D"):
        B = B + D
    if (C == "L"):
        B = B - 1
    if (C == "R"):
        B = B + 1
    return B



def main():

    win_a=0
    win_b=0
    last_turn=None
    print("\n"*40)
    print("------------------------------WELCOME TO ONE OF THE OLDEST *GAME CHEROKEE BASEBALL*-------------------------------------- ")
    print("\n")
    user_input=input("Press Y to play: ")
    # for x in range(8,11):

    #FOR ROUND NUMBER 8
    print("Please wait while the game starts..........")
    for x in range(7):
        print(u"\u25A1",end=" ")
        time.sleep(0.4)
    print("")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if user_input.lower()=="y":
        #first initiating the board to level 8
        board = [46] * 200
        print("\n"*40)
        print("------------------------THIS IS THE BOARD WHICH YOU WILL BE PLAYING ON------------------------------")
        display(8, board)
        print("For the first turn of Player 1:\n"
              "-Press D to go down.\n"
              "For the first turn of Player 2:\n"
              "-Press U to go up\n"
              "Following the instructions will initialize both the players to their initial positions\n")

        initial_A=2
        initial_B=112
        a=0
        b=112
        for all in range(112,200):
            board[all]="None"
        while a!=b or b!=a or b!=initial_A or a!=initial_B:
            #player 1
            print("-------------------------------------------Player 1--------------------------------------------------")
            pos_a=input("Enter *U*, *D*, *R* Or *L*: ")
            while pos_a.upper() not in ["U","D","R","L"]:
                print("-------------------------------------------Player 1--------------------------------------------------")
                pos_a=input("Please enter *U*, *D*, *R* Or *L* only: ")
            # output_b is the position to which b is shifted
            output_a=move(8,a,pos_a.upper())
            if output_a == initial_B:
                win_a += 1
                print("Round 8 is over. Player 1 has won.\nThe score is ", win_a, ":", win_b)
                print("\n" * 30)
                break
            while output_a<0 or output_a==0 or board[output_a]==None or board[output_a]==35:
                print("-------------------------------------------Player 1--------------------------------------------------")
                print([output_a])
                pos_a=input("You're getting out of the board, please try another position: ")
                output_a=move(8,a,pos_a.upper())
            #changing the value of the dot to "A"
            board[output_a]=65
            last_turn="A"
            #changing value of A to new position
            a=output_a
            #displaying the new board
            display(8,board)
            #initializing the board to see the latest position
            # board = [46] * 200



            if a==b:
                win_a += 1
                print("\n" * 30)
                print("Round 8 is over. Player 1 has won.\nThe score is ", win_a, ":", win_b)
                break


            #player 2
            print("\n"*5)
            print("-------------------------------------------Player 2--------------------------------------------------")
            pos_b = input("Enter *U*, *D*, *R* Or *L*: ")
            while pos_b.upper() not in ["U", "D", "R", "L"]:
                print("-------------------------------------------Player 2--------------------------------------------------")
                pos_b = input("Please enter *U*, *D*, *R* Or *L* only: ")
            #output_b is the position to which b is shifted
            output_b = move(8, b, pos_b.upper())
            while board[output_b] == None or board[output_b] == 35 or output_b>112:
                print("-------------------------------------------Player 2--------------------------------------------------")
                pos_b = input("You're getting out of the board, please try another position: ")
                output_b = move(8, b, pos_b.upper())
            # changing the value of the dot to "A"
            board[output_b] = 66
            last_turn="B"
            # changing value of A to new position
            b = output_b
            # displaying the new board
            display(8, board)
            # initializing the board to see the latest position
            # board = [46] * 200

            if output_b == initial_A:
                win_b += 1
                print("\n"*30)
                print("Round 8 is over. Player 2 has won.\nThe score is ", win_a, ":", win_b)
                break

            elif b==a:
                win_b+=1
                print("\n" * 30)
                print("Round 8 is over. Player 2 has won.\nThe score is ", win_a, ":", win_b)
                break


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
        print("Please wait while the next round starts..........")
        for x in range(7):
            print(u"\u25A1", end=" ")
            time.sleep(0.4)
        print("")
        print("\n"*40)
        print("------------------------------------------ROUND 9--------------------------------------------------")
        #FOR ROUND NUMBER NINE
        # first initiating the board to level 9
        board = [46] * 200
        display(9, board)
        initial_A = 2
        initial_B = 144
        a = 0
        b = 144
        # for all in range(132, 200):
        #     board[all] = "None"
        while a != b or b != a or b != initial_A or a != initial_B:
            # player 1
            print("-------------------------------------------Player 1--------------------------------------------------")
            pos_a = input("Enter *U*, *D*, *R* Or *L*: ")
            while pos_a.upper() not in ["U", "D", "R", "L"]:
                print("-------------------------------------------Player 1--------------------------------------------------")
                pos_a = input("Please enter *U*, *D*, *R* Or *L* only: ")
            # output_b is the position to which b is shifted
            output_a = move(9, a, pos_a.upper())
            if output_a == initial_B:
                win_a += 1
                print("Round 8 is over. Player 1 has won.\nThe score is ", win_a, ":", win_b)
                break
            while output_a < 0 or output_a == 0 or board[output_a] == None or board[output_a] == 35:
                print("-------------------------------------------Player 1--------------------------------------------------")
                pos_a = input("You're getting out of the board, please try another position: ")
                output_a = move(9, a, pos_a.upper())
            # changing the value of the dot to "A"
            board[output_a] = 65
            last_turn = "A"
            # changing value of A to new position
            a = output_a
            # displaying the new board
            display(9, board)
            # initializing the board to see the latest position
            # board = [46] * 200
            if a==b:
                win_a += 1
                print("Round 9 is over. Player 1 has won.\nThe score is ", win_a, ":", win_b)
                break

            # player 2
            print("\n"*5)
            print("-------------------------------------------Player 2--------------------------------------------------")
            pos_b = input("Enter *U*, *D*, *R* Or *L*: ")
            while pos_b.upper() not in ["U", "D", "R", "L"]:
                print("-------------------------------------------Player 2--------------------------------------------------")
                pos_b = input("Please enter *U*, *D*, *R* Or *L* only: ")
            # output_b is the position to which b is shifted
            output_b = move(9, b, pos_b.upper())
            while board[output_b] == None or board[output_b] == 35 or output_b > 144:
                print( "-------------------------------------------Player 2--------------------------------------------------")
                pos_b = input("You're getting out of the board, please try another position: ")
                output_b = move(9, b, pos_b.upper())
            # changing the value of the dot to "A"
            board[output_b] = 66
            last_turn = "B"
            # changing value of A to new position
            b = output_b
            # displaying the new board
            display(9, board)
            # initializing the board to see the latest position
            # board = [46] * 200
            if output_b == initial_A:
                win_b += 1
                print("Round 9 is over. Player 2 has won.\nThe score is ", win_a, ":", win_b)
                break

            elif b == a:
                win_b += 1
                print("Round 9 is over. Player 2 has won.\nThe score is ", win_a, ":", win_b)
                break

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
        print("Please wait while the next round starts..........")
        for x in range(7):
            print(u"\u25A1", end=" ")
            time.sleep(0.4)
        print("")
        print("\n" * 40)
        print("------------------------------------------ROUND 10--------------------------------------------------")
        # FOR ROUND NUMBER NINE
        # first initiating the board to level 9
        board = [46] * 200
        display(10, board)
        initial_A = 2
        initial_B = 180
        a = 0
        b = 180
        # for all in range(132, 200):
        #     board[all] = "None"
        while a != b or b != a or b != initial_A or a != initial_B:
            # player 1
            print(
                "-------------------------------------------Player 1--------------------------------------------------")
            pos_a = input("Enter *U*, *D*, *R* Or *L*: ")
            while pos_a.upper() not in ["U", "D", "R", "L"]:
                print(
                    "-------------------------------------------Player 1--------------------------------------------------")
                pos_a = input("Please enter *U*, *D*, *R* Or *L* only: ")
            # output_b is the position to which b is shifted
            output_a = move(10, a, pos_a.upper())
            if output_a == initial_B:
                win_a += 1
                print("Round 8 is over. Player 1 has won.\nThe score is ", win_a, ":", win_b)
                break
            while output_a < 0 or output_a == 0 or board[output_a] == None or board[output_a] == 35:
                print(
                    "-------------------------------------------Player 1--------------------------------------------------")
                pos_a = input("You're getting out of the board, please try another position: ")
                output_a = move(10, a, pos_a.upper())
            # changing the value of the dot to "A"
            board[output_a] = 65
            last_turn = "A"
            # changing value of A to new position
            a = output_a
            # displaying the new board
            display(10, board)
            # initializing the board to see the latest position
            # board = [46] * 200
            if a == b:
                win_a += 1
                print("Round 10 is over. Player 1 has won.\nThe score is ", win_a, ":", win_b)
                break

            # player 2
            print("\n" * 5)
            print(
                "-------------------------------------------Player 2--------------------------------------------------")
            pos_b = input("Enter *U*, *D*, *R* Or *L*: ")
            while pos_b.upper() not in ["U", "D", "R", "L"]:
                print(
                    "-------------------------------------------Player 2--------------------------------------------------")
                pos_b = input("Please enter *U*, *D*, *R* Or *L* only: ")
            # output_b is the position to which b is shifted
            output_b = move(10, b, pos_b.upper())
            while board[output_b] == None or board[output_b] == 35 or output_b > 180:
                print(
                    "-------------------------------------------Player 2--------------------------------------------------")
                pos_b = input("You're getting out of the board, please try another position: ")
                output_b = move(10, b, pos_b.upper())
            # changing the value of the dot to "A"
            board[output_b] = 66
            last_turn = "B"
            # changing value of A to new position
            b = output_b
            # displaying the new board
            display(10, board)
            # initializing the board to see the latest position
            # board = [46] * 200
            if output_b == initial_A:
                win_b += 1
                print("Round 10 is over. Player 2 has won.\nThe score is ", win_a, ":", win_b)
                break

            elif b == a:
                win_b += 1
                print("Round 10 is over. Player 2 has won.\nThe score is ", win_a, ":", win_b)
                break

        print("\n"*40)
        print()


main()
