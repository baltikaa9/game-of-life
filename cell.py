class Cell:
    def __init__(self, x: int, y: int, size: int):
        self.__x = x
        self.__y = y
        self.__size = size

        self.__alive = False

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def alive(self) -> bool:
        return self.__alive

    def revive(self):
        self.__alive = True

    def kill(self):
        self.__alive = False

    def toggle_alive(self):
        self.__alive = not self.__alive

    def __repr__(self):
        return f'({self.x}, {self.y}) alive: {self.alive}'


if __name__ == '__main__':
    cell = Cell(10, 10, 10)
    print(cell)