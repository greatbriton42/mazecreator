from MazeDefinition import Maze
import argparse
import random
from MazeFactory import MazeFactory


def createmaze(factory, algorithm, size: [], startpos, endpos, filepath):
    if startpos < 0:
        startpos = random.randrange(1, size[0]-1)
    if endpos < 0:
        endpos = random.randrange(1, size[0]-1)
    m = Maze(size, startpos, endpos)
    m.createtop()
    [description, creator] = factory.importmaze(algorithm)
    print(description)
    m.createmiddle(creator)
    m.createbottom()
    printtofile(filepath, m)

def printtofile(filepath, maze):
    file = open(filepath, 'w')
    file.writelines(maze.getmaze())

def main():
    mf = MazeFactory()
    parser = argparse.ArgumentParser()
    parser.add_argument("fileoutput")
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    parser.add_argument("-sp", "--startposition", type=int, default=-1)
    parser.add_argument("-ep", "--endposition", type=int, default=-1)
    parser.add_argument("algorithm", help="The algorithm to be used for maze creation", choices=mf.Choices)
    args = parser.parse_args()

    createmaze(mf, args.algorithm, [args.width, args.height], args.startposition, args.endposition, args.fileoutput)


if __name__ == "__main__":
    main()
