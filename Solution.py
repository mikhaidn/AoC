class SolutionFactory:
    def __init__(self):
        self.options = {"runOnFile":WholeFileSolution,
                        "runOnLine":LineByLineSolution,
                        "runOnLineWithMap":MapByMapSolution}

    def getSolution(self,inputManager coreLogic, terminateLogic=None):
        if inputManager.functionApproach in self.options:
            solutionConstructor = self.options[inputManager.functionApproach]
            return solutionConstructor(inputManager)
        else:
            print("Shouldn't be here: double check your input booleans")
        return

class Solution:
    def __init__(self,core, terminate=None):
        self.isTerminated = False
        self.tempValue = None
        self.result = None
        self.outputBools={"aggregateResult": True, "sumResult":True}
        if core: self.coreLogic = core
        if terminate: self.terminateCondition = terminate
    
    def run(self, line):
        self.result += self.coreLogic(line)

class WholeFileSolution(Solution):
    def __init__(self,core, terminate):
        super().__init__(core, terminate)
        self.X = 0
        self.Y = 0
        self.file = None 
        self.counter = 0

    def setInput(self, input):
        self.file = input
        return

    def move(self, deltaY, deltaX):
        self.Y = (self.Y + deltaY) % len(self.file)
        self.X = (self.X + deltaX) % len(self.file[0])

    def isAtBottom(self):
        return self.Y == len(self.file)-1
    pass
    
class LineByLineSolution(Solution):
    def __init__(self,core, terminate):
        super().__init__(core, terminate)
    pass

class MapByMapSolution(Solution):
    def __init__(self, entryChar, keyValueChar, core, terminate):
        super().__init__(core,terminate)
        self.entryChar = entryChar
        self.keyValueChar = keyValueChar
    pass
    


    
