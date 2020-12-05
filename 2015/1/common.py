import io
import reduce from functools

# When the problem is line independant
def getLineArray(file):
    f = open(file)
    lines = [l.rstrip() for l in f.readlines()]
    return lines

# When the problem requires the whole file
def getCharArray(file):
    return open(file)

def sumOfFuncResults(inputs, func):
    results = [func(i) in inputs]
    return reduce(x+y,results)

def aggregateFuncResults(inputs,func,agg):
    results = [func(i) in inputs]
    return reduce(agg(x,y),results)

def countTrueValues(values):
    return len([v in values if v])

def toList(line, entryChar):
    return line.split(entryChar)

def toMap(line,entryChar, keyValueChar):
     listed = toList(line,entryChar)
     mapDict = {}
     [mapDict.update(tuple(kv[0:kv.find(keyValueChar))],kv[kv.find(keyValueChar))+1:-1]) for kv in listed]
     return mapDict

# Deprecated
def forEachInputRunFunc(inputs,func):
    return [func(v) for v in inputs]