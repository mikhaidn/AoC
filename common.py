import io
from functools import reduce

def sumOfFuncResults(inputs, func):
    results = [func(i) for i in inputs]
    return reduce(lambda x,y:x+y,results)

def aggregateFuncResults(inputs,func,agg):
    results = [func(i) for i in inputs]
    return reduce(lambda x,y: agg(x,y),results)

def countTrueValues(values):
    return[v for v in values if v]

# Deprecated
def forEachInputRunFunc(inputs,func):
    return [func(v) for v in inputs]
