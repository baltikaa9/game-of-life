import pygame
from pygame import Surface, Rect

from color import Color
from grid import Grid


def draw_grid(screen: Surface, grid: Grid) -> None:
    screen.fill(Color.Black.value)
    cell_size = grid.cell_size
    for y in range(grid.rows):
        for x in range(grid.cols):
            if grid.is_cell_alive(x, y):
                pygame.draw.rect(screen, Color.White.value, Rect(x * cell_size, y * cell_size, cell_size, cell_size))


def init_grid_cells(grid: Grid) -> Grid:
    """Создает узор на сетке (в данном случае - крест)"""
    for i in range(grid.rows):
        for j in range(grid.cols):
            if i == (grid.rows // 2 + 1) or j == (grid.cols // 2 + 1):
                grid.revive_cell(j, i)
    return grid


def main():
    pygame.init()

    rows, cols = 150, 150
    cell_size = 5
    width, height = cols * cell_size, rows * cell_size

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game of Life')
    clock = pygame.time.Clock()

    grid = init_grid_cells(Grid(rows, cols, cell_size))

    running = True
    playing = False

    while running:
        screen.fill(Color.Black.value)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                elif event.key == pygame.K_c:
                    grid = Grid(rows, cols, cell_size)
            elif pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                cell_size = grid.cell_size

                if pygame.mouse.get_pressed()[0]:
                    grid.revive_cell(x // cell_size, y // cell_size)
                elif pygame.mouse.get_pressed()[2]:
                    grid.kill_cell(x // cell_size, y // cell_size)

        if playing: grid = grid.update()

        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(100)

    pygame.quit()


if __name__ == '__main__':
    main()