from queue import PriorityQueue
# import math
import pygame


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def tracePath(cameFrom, current, draw):
    while current in cameFrom:
        current = cameFrom[current]
        current.makePath()
        draw()


def aStarSearch(draw, graph, start, end):
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
