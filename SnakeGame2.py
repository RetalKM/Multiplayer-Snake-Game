
import random
import socket
import selectors
from CircularLinkedList import CircularLinkedList
from player import Player
import threading

class SnakeGame2:
    def __init__(self , HOST, PORT):
        self.players = CircularLinkedList()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST=HOST
        self.PORT=PORT
        self.isconnected=False
        
    def roll_dice(self):
        return random.randint(1, 6)

    def start_game(self):
        print("===========================================")
        print("The two players enter your name")
        A = input("Player(A) name: ")
        B = input("Player(B) name: ")
        print("===========================================")

        playerA = Player(A)
        playerB = Player(B)

        r = random.randint(1, 10)
        print("Who will start?, Let's see")

        if r % 2 == 0:  # first roll
            print(A + "! you start")
            self.players.add_first(playerA)
            self.players.add_last(playerB)
        else:
            print(B + "! you start")
            self.players.add_first(playerB)
            self.players.add_last(playerA)

        print("===========================================")

        while playerA.get_position() < 100 and playerB.get_position() < 100:
            print("===========================================")

            num = 0
            print(f"{self.players.first().get_player_name()} enter 'R' to roll the dice")

            roll = self.run_client()
            

            if roll.upper() == "R":
                num = self.roll_dice()
                print(f"Your roll dice {num}")
            else:
                print("Invalid input. Enter 'R' to roll the dice.")

            self.players.first().set_position(num)
            num=0

            
            if(self.players.first().get_position() == 1 ):
                self.players.first().set_position(37)
            if(self.players.first().get_position() == 4):
                self.players.first().set_position(10)
            if(self.players.first().get_position() == 8):
                self.players.first().set_position(22)
            if(self.players.first().get_position() == 21):
                self.players.first().set_position(21)
            if(self.players.first().get_position() == 28):
                self.players.first().set_position(48)
            if(self.players.first().get_position() == 50):
                self.players.first().set_position(17)
            if(self.players.first().get_position()== 80):
                self.players.first().set_position(19)
            if(self.players.first().get_position()==71):
                self.players.first().set_position(21)
            
            
            if(self.players.first().get_position()== 36):
                self.players.first().set_position(-30)
            if(self.players.first().get_position() == 62):
                self.players.first().set_position(-44)
            if(self.players.first().get_position() == 48):
                self.players.first().set_position(-22)
            if(self.players.first().get_position() == 32):
                self.players.first().set_position(-22)
            if(self.players.first().get_position() == 88):
                self.players.first().set_position(-64)
            if(self.players.first().get_position() == 95):
                self.players.first().set_position(-39)
            if(self.players.first().get_position() == 97):
                self.players.first().set_position(-19)
        

            if self.players.first().get_position() > 100:
                print(f"{self.players.first().get_player_name()} is in position 100 ")
            else:
                print(f"{self.players.first().get_player_name()} is in position {self.players.first().get_position()}")

            self.players.rotate()
        print("===========================================\n")

        if playerA.get_position() >= 100:
            print(f"||        The winner is .... player {playerA.get_player_name()}        ||\n")
        if playerB.get_position() >= 100:
            print(f"||        The winner is .... player {playerB.get_player_name()}        ||\n")
         

    def run_server(self):
        self.server_socket.bind((self.HOST,self.PORT))
        self.server_socket.listen()

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection established with {client_address}")
            
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        roll = client_socket.recv(1024).decode()
        print(f"Received roll: {roll}")

    def run_client(self):
        if not self.isconnected:
            self.client_socket.connect((self.HOST,self.PORT))
            self.isconnected=True
        roll = input("Enter 'R' to roll the dice: ")
        self.client_socket.send(roll.encode())
        return roll