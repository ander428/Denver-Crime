import numpy as np
import random as rand

class FOM:

    def __init__(self):
        self.memory = {}
        self.predictions = []

    def learn(self, dataFrame, columns):
        self.memory = dict(zip(dataFrame[columns[0]], dataFrame[columns[1]]))

    def choose(self):
        randVal = rand.random()
        total = 0
        for key, value in self.memory.items():
            uniqueVals = value
            print("Key:", key, "Value:", uniqueVals)

    def nextWord(self, key):
        values = self.memory[key]
        count = {}
        for i in values:
            if i not in count.keys():
                count[i] = 0
            count[i] += 1
        for key in count.keys():
            count[key] = count[key] / len(values)
        nw = choose(count)
        return nw
