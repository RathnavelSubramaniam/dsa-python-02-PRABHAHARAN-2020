class Position:
    def __init__(self, x=0, y=0):
        self.__x = x      # private attribute
        self.__y = y      # private attribute

    # Public method to move position
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Public method to read position
    def get_position(self):
        return (self.__x, self.__y)


class Robot:
    def __init__(self, name, x=0, y=0):
        self.__name = name                  # private attribute
        self.__position = Position(x, y)    # composition

    # Public method to move the robot
    def move(self, dx, dy):
        self.__position.move(dx, dy)

    # Public method to read robot location
    def get_location(self):
        return self.__position.get_position()

    # Optional: get robot name
    def get_name(self):
        return self.__name
