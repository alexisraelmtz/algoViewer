import pygame
from aStarSearch import aStarSearch as first
from BreadthForSearch import isConnected as second
# from depthForSearch import depthForSearch as tirdth


WIDTH = 700
GRAPH = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption(
    "AlgoViewer -- Path Finding Algorithm Propagation Visualizer By Alex Israel -- @Enroute")


START = (255, 255, 0)  # START
END = (255, 85, 51)  # END
PROPAGATION = (51, 221, 255)  # PROPAGATION
CURRENT = (179, 255, 255)  # LAST/CURRENT
OPEN = (255, 255, 255)  # OPEN
CLOSED = (0, 0, 0)  # CLOSED
PATH = (255, 255, 153)  # PATH
GRID = (230, 230, 230)  # LINES
# BLUE = (0, 255, 0)  # unused
# YELLOW = (255, 255, 0) # unused


class Node:
    def __init__(self, row, col, width, netRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = OPEN
        self.neighbours = []
        self.width = width
        self.netRows = netRows

    def getPosition(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == PROPAGATION

    def isOpen(self):
        return self.color == CURRENT

    def isWall(self):
        return self.color == CLOSED

    def isStart(self):
        return self.color == START

    def isEnd(self):
        return self.color == END

    def reset(self):
        self.color = OPEN

    #################################

    def makeClosed(self):
        self.color = PROPAGATION

    def makeOpen(self):
        self.color = CURRENT

    def makeWall(self):
        self.color = CLOSED

    def makeStart(self):
        self.color = START

    def makeEnd(self):
        self.color = END

    def makePath(self):
        self.color = PATH

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
        pygame.draw.line(window, GRID, (0, i*size), (width, i*size))
        for j in range(rows):
            pygame.draw.line(window, GRID, (j*size, 0), (j*size, width))


def draw(window, graph, rows, width):
    window.fill(OPEN)

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
                    # first.aStarSearch(lambda: draw(
                    #     window, graph, ROWS, width), graph, start, end)
                    second.breadthForSearch(lambda: draw(
                        window, graph, ROWS, width), graph, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    graph = makeGraph(ROWS, width)

    pygame.quit()


if __name__ == "__main__":
    main(GRAPH, WIDTH)
