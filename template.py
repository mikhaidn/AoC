import sys
import io
import time
from functools import reduce 
sys.path.insert(1, '..')
# Common input processing functions
import common
from Solution import *
from SolutionRunner import *
from InputManager import *


def main():
    inputFile = 'input'
    inputBools ={"LINE_SEPARATED": True,"CHAR_SEPARATED": True,"KV_SEPARATED": True}
    inputManager = common.InputManager(inputFile,inputBools)
    srf = SolutionRunnerFactory()
    sf = SolutionFactory()

    part1Solution = sf.getSolution(part1Algorithm)
    part1SolutionRunner = srf.getSolutionRunner(inputManager, part1Solution)

    part2Solution = part2()
    part2SolutionRunner = srf.getSolutionRunner(inputManager, part1())

    print(part1SolutionRunner.run())
    print(part2SolutionRunner.run())

def part1Algorithm(line):
    state = kwargs
    return state

def part2(inputManager):
    # only use one of these
    algorithmInputs {}
    runner = Runner(solver, algorithm, **algorithmInputs)
    return runner.result

def extractKeyValues(line,vert,hor):
    vals = {}
    vals["char"] = line[hor]
    return vals

if __name__ == "__main__":
    main()
