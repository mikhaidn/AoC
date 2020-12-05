import sys
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
    inputs = common.convertFileToArray(inputFile)
    return common.countTrueValues(common.forEachInputRunFunc(inputs,isValidPasswordPart1))

def part2(inputFile): 
    inputs = common.convertFileToArray(inputFile)
    return common.countTrueValues(common.forEachInputRunFunc(inputs,isValidPasswordPart2))


def extractKeyValues(input):
    vals = {}
    hyphen = input.find('-')
    firstSpace = input.find(' ')
    secondSpace = input[firstSpace+1:].find(' ') + firstSpace + 1
    vals["num1"] = int(input[0:hyphen])
    vals["num2"] = int(input[hyphen+1:firstSpace])
    vals["char"] = input [firstSpace+1]
    vals["password"] = input[secondSpace+1:]
    return vals

def isValidPasswordPart2(input):
    vals = extractKeyValues(input)
    first= vals["num1"] - 1
    second= vals["num2"] - 1
    char = vals["char"]
    word = vals["password"]
    count = 0
    if word[first] == char: count +=1
    if word[second] == char: count +=1
    return count == 1

def isValidPasswordPart1(input):
    vals = extractKeyValues(input)
    minCount = vals["num1"]
    maxCount = vals["num2"]
    char = vals["char"]
    charCount = len(list(filter(lambda c : c == char,vals["password"])))
    return charCount >= minCount and charCount <= maxCount

if __name__ == "__main__":
    main()
