#################################################################
# FILE : calculate_mathematical_expression
# WRITER : noam shabat , no.amshabat1 , 206515579
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: A simple search engine that crawl's the web.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: stackoverflow.com
# NOTES: ...
#################################################################
import sys

from board import Board
from car import Car
from helper import load_json


class Game:
    """
    this class is combining the two different classes and creating the game
    itself.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.continue_playing = True
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you, and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        print(self.__board)
        exit_msg = "for exiting the game insert the key '!' "
        error_msg = "you have inserted an invalid value! please try again. "
        option_moves = "the following command's to move are: up:u , down:d, left:l & right:r."
        print(option_moves)
        print(exit_msg)
        player_input = input(
            "please insert the name of the car and the move that you want to do by using ',' between them: ")
        if player_input == "!":
            print("Thanks for playing!!!")
            self.continue_playing = False
            return
        if "," not in player_input:
            print(error_msg)
            return
        if player_input[0] == "," or player_input[-1] == ",":
            print(error_msg)
            return
        color, direction = player_input.split(",")
        if self.__board.move_car(color, direction):
            print("good job!")
        else:
            print(error_msg)
    
        if self.__board.cell_content(
                self.__board.target_location()) is not None:
            print("congratulations you have won the game!!!")
            self.continue_playing = False

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while self.continue_playing:
            self.__single_turn()


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    car_config = load_json(sys.argv[1])
    b = Board()
    for car in car_config:
        if car not in {"R", "G", "W", "O", "B", "Y"}:
            continue
        orientation = car_config[car][2]
        if orientation not in {0, 1}:
            continue
        loc = (car_config[car][1][0], car_config[car][1][1])
        length = car_config[car][0]
        if length > 4 or length < 2:
            continue
        new_car = Car(car, length, loc, orientation)
        b.add_car(new_car)
    g = Game(b)
    g.play()
