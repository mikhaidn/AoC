class SolutionRunnerFactory():
        def __init__(self):
            self.options = {"runOnFile":WholeFileSolutionRunner,
                            "runOnLine":LineByLineSolutionRunner,
                            "runOnLineWithMap":MapByMapSolutionRunner}

        def getSolutionRunner(self, inputManager, solution):
            if inputManager.functionApproach in self.options:
                solutionRunnerConstructor = self.options[inputManager.functionApproach]
                return solutionRunnerConstructor(inputManager,solution)
            else:
                print("Shouldn't be here: double check your input booleans")
            return

class SolutionRunner:
    def __init__(self, inputManager, solution):
        self.inputManager = inputManager
        self.inputs = inputManager.inputs
        self.solution = solution

    def run(self):
        return None

class MapByMapSolutionRunner(SolutionRunner):
    def __init__(self, inputManager, solution):
        super().__init__(inputManager,solution)
        self.entryChar = solution.entryChar
        self.keyValueChar = solution.keyValueChar
        self.inputs = self._convertInputsToMapArray()
        # When the problem can be broken down to a map per line
    
    def _convertInputsToMapArray(self):
        return [self._convertLineToMapArray(line) for line in self.inputs]

    def _convertLineToMapArray(self,line):
        listed = line.split(self.solution.entryChar)
        mapDict = {}
        [mapDict.update({kv[0:kv.find(self.keyValueChar)]: kv[kv.find(self.keyValueChar)+1:-1]}) for kv in listed]
        return mapDict

    def mapByMapSolution(self):
        results = [self.solution.run(map) for maps in self.inputManager.inputs]
        return self.solution.result

    def run(self):
        return self.mapByMapSolution()
    pass
        
class LineByLineSolutionRunner(SolutionRunner):
    def __init__(self, inputManager, solution):
        super().__init__(inputManager,solution)

    def lineByLineSolution(self):
        results = [self.solution.run(line) for line in self.inputs]
        return self.solution.reduceResults(results)
    def run(self):
        return self.lineByLineSolution()
    pass

class WholeFileSolutionRunner(SolutionRunner):
    def __init__(self, inputManager, solution):
        super().__init__(inputManager,solution)
        
    def wholeFileSolution(self):
        self.solution.setInput(self.inputs)
        while (not self.solution.terminateCondition()):
            self.solution.run(None)
        return self.solution.result

    def run(self):
        return self.wholeFileSolution()
    