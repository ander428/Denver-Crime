import numpy as np
import random as rand

class FOM:

    def __init__(self, data):
        lean(data)
        self.memory = {}

    def learn(data):
        for x, y in data:
            if x not in self.memory.keys():
                memory[x] = []
            self.memory[x].append(y)

    def choose(dict):
        randVal = rand.random()
        total = 0
        for key, value in dict.items():
            total += value
            if randVal <= total:
                return key

    def nextWord(key):
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
