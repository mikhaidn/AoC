import functools
import time
import sys
sys.path.insert(1, '..')
# Common input processing functions
import common

def main():
    inputFile = 'input'
    val1 = part1(inputFile)
    print("part 1: ",val1)
    # val2 = part2(inputFile)
    # print("part 2: ",val2)

def part1(inputFile):
    fileReader = common.getFileReader(inputFile)
    return reportRepairCalculator(2020,2,fileReader)

def part2(inputFile):
    fileReader = common.getFileReader(inputFile)
    return reportRepairCalculator(2020,3,fileReader)

def reportRepairCalculator(goal, magicLength, fileReader):
    paths = {}
    paths[goal] = []
    while(True):
        current = fileReader.readline().strip()
        if len(current) > 1:
            icurrent=int(current)
        else:
            break
        keys = list(filter(lambda key : key >= icurrent and (len( paths[key]) < magicLength), paths.keys()))
        newRoute = lambda key: (key-icurrent, paths[key] + [icurrent])
        
        updates = list(map(newRoute,keys))
        upFiltered = list(filter(lambda x: x[0] not in paths, updates))
        paths.update(upFiltered)
        if 0 in paths:
            if len(paths[0]) != magicLength:
                paths.pop(0, None)
            else: 
                return functools.reduce(lambda x,y: x*y,paths[0])

if __name__ == "__main__":
    main()
