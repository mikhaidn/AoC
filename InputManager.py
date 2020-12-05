
class InputManager:
    def __init__(self,inputFile,inputParams, outputBools):
        self.file = inputFile
        self.inputParams = inputParams
        self.outputBools = outputBools
        # self.inputs = self._generateInputs()
        self.functionApproach = self._getFunctionApproach()

    def _generateInputs(self):
        if not self.inputParams["LINE_SEPARATED"]: # process whole file at once
            return self._getWholeFileAsOneInput()
        elif not self.inputParams["CHAR_SEPARATED"]: # scan each line per algorithm
            return self._getFileAsLineArray()
        elif "KV_SEPARATED": # process map later
            return self._getFileAsLineArray()
        print("Shouldn't be here: double check your input booleans")
        return 
    
    def _getFunctionApproach(self):
        if not self.inputParams["LINE_SEPARATED"]: # process whole file at once
            return "runOnFile"
        elif not self.inputParams["CHAR_SEPARATED"]: # scan each line per algorithm
            return "runOnLine"
        elif "KV_SEPARATED": # use a map to process values
            return "runOnLineWithMap"
        print("Shouldn't be here: double check your input booleans")
        return

    # When the problem is line independant
    def _getFileAsLineArray(self):
        chunkSize = max(self.inputParams.get("chunkSize", default =1),1)
        f = open(self.file)
        lines = [l.rstrip() for l in f.readlines()]
        return [lines[i:i + chunkSize] for i in range(0, len(lines), chunkSize)]

    # When the problem requires the whole file
    def _getWholeFileAsOneInput(self):
        f = open(self.file)
        lines = [l.rstrip() for l in f.readlines()]
        return [lines]