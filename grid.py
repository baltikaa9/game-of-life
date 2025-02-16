from cell import Cell


class Grid:
    def __init__(self, rows: int, cols: int, cell_size: int):
        self.__rows = rows
        self.__cols = cols
        self.__cell_size = cell_size

        self.__cells: list[list[Cell]] = [[Cell(x, y, cell_size) for x in range(cols)] for y in range(rows)]

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def cell_size(self) -> int:
        return self.__cell_size

    def revive_cell(self, x: int, y: int) -> None:
        self.__cells[y][x].revive()

    def kill_cell(self, x: int, y: int) -> None:
        self.__cells[y][x].kill()

    def is_cell_alive(self, x: int, y: int) -> bool:
        return self.__cells[y][x].alive

    def __neighbours_count(self, x: int, y: int) -> int:
        neighbours = 0
        for i in [y - 1, y, y + 1]:
            for j in [x - 1, x, x + 1]:
                if (i == y and j == x) or (i < 0) or (j < 0) or (i >= self.__rows) or (j >= self.__cols): continue

                if self.__cells[i][j].alive: neighbours += 1
        return neighbours

    def update(self) -> 'Grid':
        new_grid = Grid(self.__rows, self.__cols, self.__cell_size)
        for y in range(self.__rows):
            for x in range(self.__cols):
                if not self.is_cell_alive(x, y) and self.__neighbours_count(x, y) == 3: new_grid.revive_cell(x, y)
                elif self.is_cell_alive(x, y) and 2 <= self.__neighbours_count(x, y) <= 3: new_grid.revive_cell(x, y)
        return new_grid

    def __repr__(self) -> str:
        res = ''
        for row in range(self.__rows):
            res += ' '.join(str(int(x.alive)) for x in self.__cells[row]) + '\n'
        return res



if __name__ == '__main__':
    grid = Grid(5, 5, 5)
    grid.revive_cell(0, 0)
    grid.revive_cell(2, 0)
    grid.revive_cell(1, 1)
    grid.revive_cell(0, 2)
    grid.revive_cell(2, 2)
    print(grid)
    grid = grid.update()
    print(grid)
    grid = grid.update()
    print(grid)