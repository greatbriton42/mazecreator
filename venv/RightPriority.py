import random
import Random

def create(size, start, end):
    #middle = [[0 for i in range(size[1])] for i in range(size[0])]
    middle = Random.create(size, start, end)
    markedY = 0
    markedX = start

    # Edit the values to connect the maze
    while markedY != size[1]-2 and markedX != end:
        [top, right, bottom, left] = boundcheck(size, markedY, markedX)
        if right and random.randrange(5) == 0:
            middle[markedY][markedX+1] = 0
        else:
            right = False
        if bottom and random.randrange(5) == 0:
            middle[markedY+1][markedX] = 0
        else:
            bottom = False
        if left and random.randrange(5) == 0:
            middle[markedY][markedX - 1] = 0
        else:
            left = False

        if right:
            markedX = markedX + 1
        elif bottom:
            markedY = markedY + 1
        elif left:
            markedX = markedX - 1


    return middle

# False if neighboring point is out of bounds or not to be changed (edges)
def boundcheck(size, y, x):
    top = True
    right = True
    bottom = True
    left = True

    if y-1 < 0:
        top = False
    elif y+1 >= size[1]-2:
        bottom = False
    if x+1 >= size[0]-1:
        right = False
    elif x-1 <=0:
        left = False

    return [top, right, bottom, left]

