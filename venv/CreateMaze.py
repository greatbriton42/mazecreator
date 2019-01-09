from MazeDefinition import Maze
import argparse


def createmaze(size: [], startpos, endpos, filepath):
    m = Maze(size)
    m.createtop(startpos)
    m.createmiddle()
    m.createbottom(endpos)
    printtofile(filepath, m)

def printtofile(filepath, maze):
    file = open(filepath, 'w')
    file.writelines(maze.getmaze())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fileoutput")
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    parser.add_argument("-sp", "--startposition", type=int, default=-1)
    parser.add_argument("-ep", "--endposition", type=int, default=-1)
    args = parser.parse_args()

    createmaze([args.width, args.height], args.startposition, args.endposition, args.fileoutput)

if __name__ == "__main__":
    main()
