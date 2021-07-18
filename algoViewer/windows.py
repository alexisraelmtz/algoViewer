import pygame
import math
from queue import PriorityQueue
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"


WIDTH = 600
GRAPH = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("AlgoViewer -- Recursive Propagation Algorithms")

RED = (255, 0, 0)  # Visited
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, netRows) -> None:
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.netRow = netRows

    def getPosition(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == RED

    def isOpen(self):
        return self.color == GREEN

    def isWall(self):
        return self.color == BLACK

    def isStart(self):
        return self.color == ORANGE

    def isEnd(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color == WHITE

    #################################

    def makeClosed(self):
        self.color = RED

    def makeOpen(self):
        self.color = GREEN

    def makeWall(self):
        self.color = BLACK

    def makeStart(self):
        self.color = ORANGE

    def makeEnd(self):
        self.color = TURQUOISE

    def makePath(self):
        self.color = PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.width))

    def updateNeighbours(self, grid):
        pass

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def makeGraph(rows, width):
    graph = []
    size = width // rows
    for i in range(rows):
        graph.append([])
        for j in range(rows):
            node = Node(i, j, size, rows)
            graph[i].append(node)

    return graph


def drawGraph(window, rows, width):
    size = width//rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i*size), (width, i*size))
        for j in range(rows):
            pygame.draw.line(window, GREY, (j*size, 0), (j*size, width))


def draw(window, graph, rows, width):
    window.fill(WHITE)

    for row in graph:
        for node in row:
            node.draw(window)

    drawGraph(window, rows, width)
    pygame.display.update()


def getMousePosition(position, rows, width):
    size = width//rows
    y, x = position

    row = y//size
    col = x//size

    return row, col


def main(window, width):
    ROWS = 20
    graph = makeGraph(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        for event in pygame.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue


pygame.quit()
