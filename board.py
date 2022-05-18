#################################################################
# FILE : board.py
# WRITER : noam shabat , no.amshabat1 , 206515579
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: A simple search engine that crawl's the web.
# STUDENTS I DISCUSSED THE EXERCISE WITH:...
# WEB PAGES I USED: stackoverflow.com
# NOTES: ...
#################################################################


class Board:
    """
    this class is creating a board element to be a part of the Game as a hole &
    determined the actions regarding the roles about the board.
    """
    SIZE = 7
    FINISH_POINT = (3, 7)

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.SELF_EMPTY_VALS = {'*', "||", "_"}
        self.BOARD = [['_', '_', '_', '_', '_', '_', '_', '*'],
                      ['_', '_', '_', '_', '_', '_', '_', '*'],
                      ['_', '_', '_', '_', '_', '_', '_', '*'],
                      ['_', '_', '_', '_', '_', '_', '_', '||'],
                      ['_', '_', '_', '_', '_', '_', '_', '*'],
                      ['_', '_', '_', '_', '_', '_', '_', '*'],
                      ['_', '_', '_', '_', '_', '_', '_', '*']]

        self.cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        str_board = ""
        for row in range(len(self.BOARD)):
            str_row_board = ""
            for col in range(len(self.BOARD[row])):
                str_row_board += self.BOARD[row][col] + " "
            str_board += str_row_board + "\n"
        return str_board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        coordinates = []
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                coordinates.append((x, y))
        coordinates.append(self.FINISH_POINT)
        return coordinates

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value
        # could be.
        # [('O','d',"some description"),('R','r',"some description"),
        #  ('O','u',"some description")].
        res = []
        for car in self.cars:
            moves = car.possible_moves()
            for move, desc in moves.items():
                movi = False
                for element in car.movement_requirements(move):
                    if element not in self.cell_list():
                        movi = True
                    if self.cell_content(element) is not None:
                        movi = True
                if movi:
                    continue
                else:
                    movekey = (car.get_name(), move, desc)
                    res.append(movekey)
        return res

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return self.FINISH_POINT

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if not self.coordinate_on_board(coordinate):
            return None
        res = self.BOARD[coordinate[0]][coordinate[1]]
        if res in self.SELF_EMPTY_VALS:
            return None
        return res

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"

        if not self.car_is_valid(car):
            return False

        self.cars.append(car)
        for coord in car.car_coordinates():
            self.BOARD[coord[0]][coord[1]] = car.get_name()
        return True

    def car_is_valid(self, car):
        """
        this func is doing validation to check if a specific car is ok to
        be placed
        :param car: an object from type car
        :return: true if the car is ok to ce placed and false if not.
        """
        coords = car.car_coordinates()
        for coord in coords:
            if not self.coordinate_on_board(coord):
                return False
        for coord in coords:
            if self.cell_content(coord) is not None:
                return False
        for second_car in self.cars:
            if car.get_name() == second_car.get_name():
                return False
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for car in self.cars:
            if name == car.get_name():
                if not self.move_car_is_valid(car, movekey):
                    return False
                move_list = car.car_coordinates()
                for move in move_list:
                    self.BOARD[move[0]][move[1]] = "_"
                try_move = car.move(movekey)
                for coord in car.car_coordinates():
                    self.BOARD[coord[0]][coord[1]] = car.get_name()
                return try_move
        return False

    def move_car_is_valid(self, car, movekey):
        """
        this func is checking if a move to a car can be done.
        :param car: an object from type car
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        move_list = car.movement_requirements(movekey)
        for move in move_list:
            if move == self.FINISH_POINT:
                return True
            if not move in self.cell_list():
                return False
            if self.cell_content(move) is not None:
                return False
        return True

    def coordinate_on_board(self, coordinate):
        """
        this func is checking if a car object is place outside the board.
        :param coordinate: the coordinate of location of the car.
        :return: true if the car is placed right and false if not.
        """
        if coordinate is self.FINISH_POINT:
            return True
        if coordinate[0] >= self.SIZE or coordinate[1] >= self.SIZE:
            return False
        if coordinate[0] < 0 or coordinate[1] < 0:
            return False
        return True


if __name__ == '__main__':
    pass
