"""
Purpose:
A program to implement a guessing game. 

Game rules
1. A game co-ordinator inputs the number of players to a game
2. At the start of the game, all players are asked for their names
3. At the start of each round, a new magic number between 1 and 10 (not visible to the players) is generated
4. Each player is asked for their guess
5. The player(s) with the closest guesses win 1 point
6. The user then has a choice to continue to the next round or stop the game
7. At the end of the game, the total points scored by each player is listed and the winner(s) is announced.

Author: Preedhi Vivek
Date: 30/07/2019

"""
import random 
from collections import Counter

class UserInput():

    # Initialize the variables to be used in this class
    def __init__(self):
        self.no_of_players = 0
        self.player_name = ""
        self.player_data = {}
        
    # method to get the number of users and user names 
    def get_user_input(self):
        print("Enter the number of players:")
        while True:
            try:
                self.no_of_players = int(input())
                if isinstance(self.no_of_players,int) and (self.no_of_players == 1):
                    print("Atleast two players are required to play this guessing game!\n")
                    print("Enter the number of players (between 1 to 5):")    
                elif isinstance(self.no_of_players,int) and (self.no_of_players > 0) and (self.no_of_players <= 5):
                    break
                elif isinstance(self.no_of_players,int) and (self.no_of_players < 0):    
                    print("Please enter a positive integer (between 1 to 5)!")
                elif isinstance(self.no_of_players,int) and (self.no_of_players > 5):
                    print("Please enter a positive integer (between 1 to 5)!")
            except ValueError:
                print("Please enter a positive integer (between 1 to 5)!")    
        
        for  i in range(self.no_of_players):
            j = i+1
            print("Enter the name of player%d: "%j)
            while True:
                try:
                    self.player_name = str(input())
                    if isinstance(self.player_name,str) and (self.player_name.isalpha()):
                        break
                    elif isinstance(self.player_name,str) and (self.player_name.isdigit()):
                        print("Please enter a valid name!")
                    else:    
                        print("Please enter a valid name!")
                except ValueError:
                    print("Please enter a valid name!")    
        
            self.player_data.update({self.player_name:0})

        return self.no_of_players, self.player_data        

class GenerateRandom():

 # Initialize the variables to be used in this class
    def __init__(self):
        self.magic_number = 0

    def get_random_integer(self):
        self.magic_number = random.randint(1, 10)
        return self.magic_number
                
class GetUserGuess():

    # Initialize the variables to be used in this class
    def __init__(self):
        self.guess_data = {}
        self.guess_number = 0

    def get_user_guess(self, player_info,player_count):
        i =1
        for key in player_info.keys() : 
            print("Player %d - Enter your guess: "%i)
            while True:
                try:
                    self.guess_number = int(input())
                    if isinstance(self.guess_number,int) and self.guess_number > 0 and self.guess_number <= 10:
                        break
                    elif (self.guess_number < 0) :
                        print("Enter a positive integer between 1 and 10 (inclusive) to guess!")    
                    elif isinstance(self.guess_number,int) and self.guess_number >10 :
                     print("Enter an integer between 1 and 10 (inclusive) to guess! ")
                except ValueError:
                 print("Enter a positive integer between 1 and 10 (inclusive) to guess!")    
            i = i+1    
            self.guess_data.update({key:self.guess_number})
        
        return self.guess_data

class ClosestGuesser() :
    def __init__(self):
        self.difference = 0
        self.difference_info = {}
        self.closest_guess = ()
        

    def find_the_closest_guess(self, magic_number, guess_info):
        for key,value in guess_info.items():
            if (magic_number >= value)  :
                self.difference = magic_number - value
            elif (magic_number < value):
                self.difference = value - magic_number
            self.difference_info.update({key:self.difference})

        self.closest_guess = min(self.difference_info.items(), key=(lambda k: k[1]))
              
        return self.closest_guess

class AddPoint() :
    def add_point_to_score(self, closest_guess_data, player_data):
        for key,value in player_data.items():
            if (closest_guess_data[0] == key) :
                value = int(value) + 1
                player_data.update({key:value})    
        return player_data



# Program starts here
if __name__ == "__main__":
    print("\n PLAY GUESSING GAME!! \n")

    # obj1 is an object of class UserInput
    obj1 = UserInput()
    # Call the method to get the user input 
    player_count, player_info = obj1.get_user_input()
    #print("Player Info: ", player_info)
    print ("\nRound 1")
    round_count = 1
    while True:

        if (round_count > 1):        
            print("Round %d"%round_count)
        # obj2 is an object of class GenerateRandom
        obj2 = GenerateRandom()
        #Call the method to generate a random number between 1 to 10
        magic_number = obj2.get_random_integer()
        #print("Magic Number: ", magic_number)

        # obj3 is an object of class GetUSerGuess
        obj3 = GetUserGuess()
        #Call the method to get the user guesses
        guess_info = obj3.get_user_guess(player_info, player_count)
        #print("Guess Info: ", guess_info)

        # obj4 is an object of class ClosestGuesser
        obj4 = ClosestGuesser()
        #Call the method to find the user whose guess was the closest
        closest_guess_info = obj4.find_the_closest_guess(magic_number,guess_info)
        #print("Closest Guess Info: ", closest_guess_info)

        # obj5 is an object of class AddPoint
        obj5 = AddPoint()
        #Call the method to add a point to the closest guesser
        updated_player_info = obj5.add_point_to_score(closest_guess_info, player_info)
        print("Score Board for round %d: "%round_count,updated_player_info)

        
        while True:    
            print("\n Do you wish to continue? Y/N:")
            try:
                next_round = str(input())
                if isinstance(next_round,str) and  (len(next_round)==1) and (next_round.isupper()) and (next_round == 'Y'):
                    round_count += 1
                    set_exit = 0
                    break
                elif isinstance(next_round,str) and  (len(next_round)==1) and (next_round.isupper()) and (next_round == 'N'):
                    set_exit = 1 
                    break 
                elif isinstance(next_round,str) and (len(next_round)!=1):
                    print("Enter only Y or N")
                else :
                    print("Enter only Y or N")    

            except ValueError:
                print("Enter only Y or N")
        if (set_exit == 1):
            break
    
    print("\n The Winner of this Guessing Game is:  %s"%closest_guess_info[0])
    print("\n Congrats %s!!"%closest_guess_info[0])