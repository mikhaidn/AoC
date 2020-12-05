import sys
import io
import time
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
    inputs = common.convertFileToArray(inputFile)
    return scannerSolution(inputs,-1,1)


def part2(inputFile):
    return None

def scannerSolution(inputs,goal,a):
    flat_list = [item for sublist in inputs for item in sublist]
    counter =0
    iter = 0
    for c in flat_list:
        iter +=1
        if c == "(":counter +=1
        else: counter -=1
        if counter == goal: return iter

    return 

def extractKeyValues(line,vert,hor):
    vals = {}
    vals["char"] = line[hor]
    return vals

if __name__ == "__main__":
    main()
