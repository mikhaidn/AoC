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

    part1Solution = sf.getSolution(inputManager, part1Algorithm, terminatelogic = None)
    part1SolutionRunner = srf.getSolutionRunner(inputManager, part1Solution)

def part1Algorithm(line):
    mandatory =["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    optional = ["cid"]
    if 7 == len([x in mandatory for x in line.keys]):
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()
