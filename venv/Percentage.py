import random

def create(size, start, end):
    middle = [[1 for i in range(size[1])] for i in range(size[0])]
    for y in range(0, size[1]-2):
        for x in range(0, size[0]):
            if x != 0 or x != size[0]-1:
                if x == start and y == 0:
                    middle[y][x] = 0
                elif y == size[1]-3 and x == end:
                    middle[y][x] = 0
                else:
                    middle[y][x] = random.randrange(2)
    return middle