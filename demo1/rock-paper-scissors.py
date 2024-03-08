from enum import Enum
import random

class Element(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    NULL = 3

class Round:
    def __init__(self) :
        self.winner = 0

class Player:
    def __init__(self, name) :
        self.name = name
        self.won = 0
        self.play = Element.NULL

class Game:
    def __init__(self) :
        self.name = "ROCK PAPER SCISSORS"
        print("------------------------")
        print("WELCOME BACK!")
        print("------------------------")
        self.gameOver = False
        self.player1 = Player(self.getPlayerName(1).upper())
        self.player2 = Player(self.getPlayerName(2).upper())
        self.results = "\n------------------------\nGAME FINISHED - RESULTS:\n\n"
        roundNo = 1
        exit = False
        
        while(True):
            print("------------------------")
            print("\nROUND", roundNo, "\n")
            self.Play(roundNo)
            roundNo += 1
            print("------------------------")
            while(True):
                again = input("\nPlay again? Y/YES N/NO: ").lower()
                if again.lower() == "n":
                    exit = True
                    break
                elif again.lower() == "y":
                    break
            if exit:
                break

        self.results += "------------------------\n"
        print(self.results)
        print("------------------------")
        print("GOODBYE!")
        print("------------------------")
    
    def getPlayerName(self, num) :
        return input("GIVE PLAYER {} NAME: ".format(num))
    
    def Play(self, roundNo):
            while True:
                play = input(self.player1.name + " CHOOSE YOUR MOVE: R/Rock, P/Paper, S/Scissors: ")
                play = play.upper()
                if play == "R":
                    self.player1.play = Element(0)
                    break
                elif play == "P":
                    self.player1.play = Element(1)
                    break
                elif play == "S":
                    self.player1.play = Element(2)
                    break
            
            while True:
                play = input(self.player2.name + " CHOOSE YOUR MOVE: R/Rock, P/Paper, S/Scissors: ")
                play = play.upper()
                if play == "R":
                    self.player2.play = Element(0)
                    break
                elif play == "P":
                    self.player2.play = Element(1)
                    break
                elif play == "S":
                    self.player2.play = Element(2)
                    break
                
            print("\n", self.player1.name, ":", self.player1.play.name)
            print("\n", self.player2.name, ":", self.player2.play.name)
            if self.player1.play == self.player2.play:
                print("\nRESULT: TIE!") 
                self.results += "ROUND " + str(roundNo) + " RESULT: TIE" + "\n"
            elif (self.player1.play == Element.ROCK and self.player2.play == Element.SCISSORS) or (self.player1.play == Element.PAPER and self.player2.play == Element.ROCK) or (self.player1.play == Element.SCISSORS and self.player2.play == Element.PAPER) :
                print("\nRESULT:", self.player1.name)
                self.results += "ROUND " + str(roundNo) + " RESULT: " + self.player1.name + "\n"
                print("\n------------------------")
                print(self.player1.name, "WON! CONGRATULATIONS!")
                self.player1.won += 1
            else:
                print("\nRESULT:", self.player2.name)
                self.results += "ROUND " + str(roundNo) + " RESULT: " + self.player2.name+ "\n"
                print("\n------------------------")
                print(self.player2.name, "WON! CONGRATULATIONS!")
                self.player2.won += 1

Game() 