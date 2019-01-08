from PIL import Image
import argparse
import math


def create(fileinput, fileoutput, size):
    print("Reading File:")
    imap = []
    with open(fileinput) as mapping:
        for line in mapping:
            characters = line.split()
            for char in characters:
                imap.append(int(char))

    print("File length: ", len(imap))
    print("Calculating Size...", end=" ")
    if size[0] <= 0 and size[1] <= 0:
        size[0] = int(math.sqrt(len(imap)))
        size[1] = int(len(imap)/size[0])
    elif size[0] > 0 and size[1] <= 0:
        size[1] = int(len(imap)/size[0])
    elif size[0] <= 0 and size[1] > 0:
        size[0] = int(len(imap)/size[1])
    print(size)

    print("Drawing Image")
    im = Image.new("RGB", size, color="black")
    impixels = im.load()
    for y in range(0, size[1]):
        for x in range(0, size[0]):
            if imap[y*size[0] + x] == 1:
                r = 0
            else:
                r = 1
            px = (255*r, 255*r, 255*r)
            impixels[x,y] = px
    im.save(fileoutput)
    print("Image Completed")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("outputfile")
    parser.add_argument("-x", "--width", type=int, default=-1)
    parser.add_argument("-y", "--height", type=int, default=-1)
    args = parser.parse_args()

    create(args.inputfile, args.outputfile, [args.width, args.height])


if __name__ == "__main__":
    main()
