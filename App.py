import sys
from SnakeGame2 import SnakeGame2
import threading


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please enter Host and Port ")
        sys.exit(0)
    host, port = sys.argv[1], int(sys.argv[2])
    game = SnakeGame2(HOST=host,PORT=port)
    print("-- Welcome to our game, which is a snake and ladders game --\n")
    print("THE RULES OF THE GAME ARE:")
    print("Every player will take turns to roll the dice")
    print("The first player that reaches the highest space on the board, 100, wins")
    print("If you land on any snake head, you will go down to its tail")
    print("If you land at the beginning of a ladder, you will go up to the ladder's top")
    print("If you roll a six, then you get an extra turn\n")
    
    print("Snake symbol: (@)\nLadder symbol: (^)")
    print(
            "----------------------------------------------\n"
            + "100 99  98   @  96  @   94  93  92  91\n"
            + "81  82  83  84  85  86  87  @   89  90 \n"
            + "41  42  43  44  45  46  47  @   49  ^  \n"
            + "^   79  78  77  76  75  74  73  72  ^  \n"
            + "61  @   63  64  65  66  67  68  69  70 \n"
            + "60  59  58  57  56  55  54  53  52  51 \n"
            + "40  39  38  37  @   35  34  33  @   31 \n"
            + "^   22  23  24  25  26  27  ^   29  30 \n"
            + "20  19  18  17  16  15  14  13  12  11 \n"
            + "^   2   3   ^   5   6   7   ^   9   10\n"
            + "----------------------------------------------\n"
    )
    
    exit_game = True
    while exit_game:
        print("Please choose how you want to play:")
        print("1.with your friend\t3. exit")
    
        answer = int(input())
            
        if answer == 1:
            server_thread = threading.Thread(target=game.run_server)
            server_thread.start()

            game.start_game()
        elif answer == 2:
            exit_game = False
            print("Goodbye")
        else:
            print(f"{answer} is an invalid number. Please try again.")

    
