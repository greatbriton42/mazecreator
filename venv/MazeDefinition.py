import random


class Maze:
    def __init__(self, size: []):
        self.size = size
        self.top = [0 for i in range(self.size[0])]
        self.middle = [[0 for i in range(self.size[1])] for i in range(self.size[0])]
        self.bottom = [0 for i in range(self.size[0])]

    def createtop(self, startposition):
        # Choose a random start position
        if startposition < 0:
            pos = random.randrange(self.size[0])
            for x in range(0, self.size[0]):
                if x == pos:
                    self.top[x] = 0
                else:
                    self.top[x] = 1
        # Create start position at passed value
        else:
            for x in range(0, self.size[0]):
                if x == startposition:
                    self.top[x] = 0
                else:
                    self.top[x] = 1

    def createbottom(self, endposition):
        # Choose a random start position
        if endposition < 0:
            pos = random.randrange(self.size[0])
            for x in range(0, self.size[0]):
                if x == pos:
                    self.bottom[x] = 0
                else:
                    self.bottom[x] = 1
        # Create start position at passed value
        else:
            for x in range(0, self.size[0]):
                if x == endposition:
                    self.bottom[x] = 0
                else:
                    self.bottom[x] = 1

    def createmiddle(self):
        for y in range(0, self.size[1]-2):
            for x in range(0, self.size[0]):
                if x == 0 or x == self.size[0]-1:
                    self.middle[y][x] = 1
                else:
                    self.middle[y][x] = random.randrange(2)

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
