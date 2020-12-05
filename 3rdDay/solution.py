import sys
import io
import time
import functools
sys.path.insert(1, '..')
# Common input processing functions
import common

def main():
    inputFile = 'input'
    
    val1 = part1(inputFile)
    print("part 1: ",val1)
    val2 = part2(inputFile)
    print("part 2: ",val2)

def part1(inputFile):
    # only use one of these
    return scannerSolution(inputFile,3,1)

def part2(inputFile):
    # only use one of these
    return scannerSolution(inputFile,1,1) * scannerSolution(inputFile,3,1) * scannerSolution(inputFile,5,1) * scannerSolution(inputFile,7,1) * scannerSolution(inputFile,1,2)

def scannerSolution(inputFile,right,down):
    fileReader = common.getFileReader(inputFile)

    vert = 0
    hor = 0
    treesEncountered = 0
    while(True):
        current = fileReader.readline().strip()
        if len(current) > 1:
            line=current
        else:
            break
        if vert % down != 0: 
            print(vert)
            vert = (vert + 1)
            continue
        if line[hor] == '#':
            treesEncountered +=1
        hor = (hor + right) % len(line)
        vert = (vert + 1)
    
    return treesEncountered

if __name__ == "__main__":
    main()
