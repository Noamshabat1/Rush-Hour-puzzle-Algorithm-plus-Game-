class Car:
    """
    this class is creating a car element to be a part of the Game.
    """
    HORIZONTAL = 1
    VERTICAL = 0

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__length = length
        self.__orientation = orientation
        self.__name = name
        self.__location = location

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        list_of_coordinates = [self.__location]
        if self.__orientation == self.HORIZONTAL:
            for i in range(1, self.__length):
                list_of_coordinates.append(
                    (self.__location[0], self.__location[1] + i))

        elif self.__orientation == self.VERTICAL:
            for i in range(1, self.__length):
                list_of_coordinates.append(
                    (self.__location[0] + i, self.__location[1]))

        return list_of_coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        moves_dic_vertical = {
            'u': "the cor is moving up.",
            'd': " the car is moving down."
        }

        moves_dic_horizontal = {
            'l': "the cor is moving left.",
            'r': " the car is moving right."
        }
        if self.__orientation == self.HORIZONTAL:
            return moves_dic_horizontal
        if self.__orientation == self.VERTICAL:
            return moves_dic_vertical

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        # [(0,0),(0,1),(0,2)
        # (1,0),(1,1),(1,2),
        # (2,0),(2,1)(2,2),]
        if self.__orientation == self.HORIZONTAL:
            if movekey == 'r':
                return [(self.__location[0], self.__location[1] + self.__length)]
            if movekey == 'l':
                return [(self.__location[0], self.__location[1] - 1)]
        if self.__orientation == self.VERTICAL:
            if movekey == 'd':
                return [(self.__location[0] + self.__length, self.__location[1])]
            if movekey == 'u':
                return [(self.__location[0] - 1, self.__location[1])]
        return []

    def move(self, movekey):

        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey not in self.possible_moves():
            return False

        if movekey == 'r':
            self.__location = (self.__location[0], self.__location[1] + 1)
            return True
        if movekey == 'l':
            self.__location = (self.__location[0], self.__location[1] - 1)
            return True
        if movekey == 'd':
            self.__location = (self.__location[0] + 1, self.__location[1])
            return True
        if movekey == 'u':
            self.__location = (self.__location[0] - 1, self.__location[1])
            return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
