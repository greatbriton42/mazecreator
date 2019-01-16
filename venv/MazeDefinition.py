import random


class Maze:
    def __init__(self, size: [], start, end):
        self.size = size
        self.start = start
        self.end = end
        self.top = [0 for i in range(self.size[0])]
        self.middle = [[0 for i in range(self.size[1])] for i in range(self.size[0])]
        self.bottom = [0 for i in range(self.size[0])]

    def createtop(self):
        for x in range(0, self.size[0]):
            if x == self.start:
                self.top[x] = 0
            else:
                self.top[x] = 1

    def createbottom(self):
        # Create start position at passed value
        for x in range(0, self.size[0]):
            if x == self.end:
                self.bottom[x] = 0
            else:
                self.bottom[x] = 1

    def createmiddle(self, algorithm):
        self.middle = algorithm(self.size, self.start, self.end)

    def getmaze(self) -> [str]:
        maze = []
        for i in range(0, self.size[0]):
            maze.append(str(self.top[i]))
        for y in range(0, self.size[1]-2):
            for x in range(0, self.size[0]):
                maze.append(str(self.middle[y][x]))
        for i in range(0, self.size[0]):
            maze.append(str(self.bottom[i]))
        return maze

    def printmaze(self):
        print(self.top)
        print(self.middle)
        print(self.bottom)
