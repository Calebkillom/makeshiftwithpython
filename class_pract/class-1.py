#!/usr/bin/python3
# getters and setters example

class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

        @property
        def height(self):
            print("Retrieving the height")
            return self.__height

        @height.setter
        def height(self, value):
            if value.isdigit:
                self.__height = value
            else:
                print("Please enter only number for height")

        @property
        def width(self):
            print("Retrieving the width")
            return self.__width

        @width.setter
        def width(self, value):
            if value.isdigit():
                self.__width = value
            else:
                print("please only enter numbers for width")

    def getArea(self):
            return int(self.width) * int(self.height)

def main():
    aSquare = Square()

    height = input("Enter Height: ")
    width = input("Enter width: ")

    aSquare.height = height
    aSquare.width = width

    print("Height: ", aSquare.height)
    print("Width: ", aSquare.width)
    print("The Area is: ", aSquare.getArea())


if __name__ == "__main__":
    main()
