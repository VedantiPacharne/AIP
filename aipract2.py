import pygame
import heapq
import time

# Initialize Pygame
pygame.init()

# Constants
ROWS, COLS = 8, 8
TILE_SIZE = 60
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE
FPS = 30
DELAY = 90  # milliseconds

# Colors
WHITE = (255, 255, 255)
BLACK = (40, 40, 40)
GRAY = (160, 160, 160)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 102, 204)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Refined A* PAC-MAN Search")
clock = pygame.time.Clock()

# Directions: up, down, left, right
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def draw_cell(pos, color, text=None):
    x, y = pos[1]*TILE_SIZE, pos[0]*TILE_SIZE
    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, GRAY, rect, 1)

    if text:
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (x + 15, y + 15))
    pygame.display.update()
    pygame.time.delay(DELAY)

def draw_grid(grid, start, goal):
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            pos = (row, col)
            if grid[row][col] == 1:
                draw_cell(pos, BLACK)
            elif pos == start:
                draw_cell(pos, GREEN, "P")  # PAC-MAN
            elif pos == goal:
                draw_cell(pos, RED, "G")  # Goal
            else:
                draw_cell(pos, WHITE)
    pygame.display.update()

def a_star(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, Node(start, None, 0, manhattan_distance(start, goal)))
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)

        if current.position == goal:
            return reconstruct_path(current)

        closed_set.add(current.position)

        for d in DIRS:
            neighbor = (current.position[0] + d[0], current.position[1] + d[1])
            if (0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS and
                grid[neighbor[0]][neighbor[1]] != 1 and
                neighbor not in closed_set):

                g = current.g + 1
                h = manhattan_distance(neighbor, goal)
                node = Node(neighbor, current, g, h)
                heapq.heappush(open_set, node)
                if neighbor != goal:
                    draw_cell(neighbor, CYAN)  # Visiting

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        if node.parent:  # skip start
            draw_cell(node.position, YELLOW)
        node = node.parent
    return path[::-1]

def main():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (7, 7)

    draw_grid(grid, start, goal)
    path = a_star(grid, start, goal)

    font = pygame.font.SysFont(None, 28)
    if path:
        msg = f"Path found! Steps: {len(path)}"
        print(msg)
    else:
        msg = "No path found."

    # Display message
    text_surface = font.render(msg, True, BLUE)
    screen.blit(text_surface, (10, HEIGHT - 30))
    pygame.display.update()

    # Wait for user to close window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
