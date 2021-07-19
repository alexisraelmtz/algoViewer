import pygame
import math
from queue import PriorityQueue
import time


WIDTH = 800
GRAPH = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("AlgoViewer -- Recursive Propagation Algorithms")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, netRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.netRows = netRows

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
        self.color = WHITE

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

    def updateNeighbours(self, graph):
        self.neighbours = []
        # DOWN
        if self.row < self.netRows - 1 and not graph[self.row + 1][self.col].isWall():
            self.neighbours.append(graph[self.row + 1][self.col])
        # UP
        if self.row > 0 and not graph[self.row - 1][self.col].isWall():
            self.neighbours.append(graph[self.row - 1][self.col])
        # RIGHT
        if self.col < self.netRows - 1 and not graph[self.row][self.col + 1].isWall():
            self.neighbours.append(graph[self.row][self.col + 1])
        # LEFT
        if self.col > 0 and not graph[self.row][self.col - 1].isWall():
            self.neighbours.append(graph[self.row][self.col - 1])

    def __lt__(self, other):
        return False


#################################


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def tracePath(cameFrom, current, draw):
    while current in cameFrom:
        current = cameFrom[current]
        current.makePath()
        draw()


def aStarAlgo(draw, graph, start, end):
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))
    cameFrom = {}
    gScore = {node: float("inf") for row in graph for node in row}
    gScore[start] = 0
    fScore = {node: float("inf") for row in graph for node in row}
    fScore[start] = h(start.getPosition(), end.getPosition())

    openSetDict = {start}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = openSet.get()[2]
        openSetDict.remove(current)

        if current == end:
            tracePath(cameFrom, end, draw)
            end.makeEnd()
            return True

        for neighbour in current.neighbours:
            gTempScore = gScore[current] + 1

            if gTempScore < gScore[neighbour]:
                cameFrom[neighbour] = current
                gScore[neighbour] = gTempScore
                fScore[neighbour] = gTempScore + \
                    h(neighbour.getPosition(), end.getPosition())
                if neighbour not in openSetDict:
                    count += 1
                    openSet.put((fScore[neighbour], count, neighbour))
                    openSetDict.add(neighbour)
                    neighbour.makeOpen()
        # time.sleep(0.1)
        draw()

        if current != start:
            current.makeClosed()

    return False


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
    ROWS = 50
    graph = makeGraph(ROWS, width)

    start = None
    end = None

    run = True

    while run:
        draw(window, graph, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left
                position = pygame.mouse.get_pos()
                row, col = getMousePosition(position, ROWS, width)
                node = graph[row][col]
                if not start and node != end:
                    start = node
                    start.makeStart()

                elif not end and node != start:
                    end = node
                    end.makeEnd()

                elif node != end and node != start:
                    node.makeWall()

            elif pygame.mouse.get_pressed()[2]:  # Right
                position = pygame.mouse.get_pos()
                row, col = getMousePosition(position, ROWS, width)
                node = graph[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    # print("Space was Pressed Down.")
                    for row in graph:
                        for node in row:
                            node.updateNeighbours(graph)
                    aStarAlgo(lambda: draw(window, graph,
                              ROWS, width), graph, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    graph = makeGraph(ROWS, width)

    pygame.quit()


if __name__ == "__main__":
    main(GRAPH, WIDTH)
