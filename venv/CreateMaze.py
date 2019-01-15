from MazeDefinition import Maze
import argparse
from MazeFactory import mazefactory


def createmaze(factory, algorithm, size: [], startpos, endpos, filepath):
    m = Maze(size)
    m.createtop(startpos)
    [description, creator] = factory.importmaze(algorithm)
    print(description)
    m.createmiddle(creator, startpos, endpos)
    m.createbottom(endpos)
    printtofile(filepath, m)

def printtofile(filepath, maze):
    file = open(filepath, 'w')
    file.writelines(maze.getmaze())

def main():
    mf = mazefactory()
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
