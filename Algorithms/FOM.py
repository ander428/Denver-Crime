# Matt Greenberg - 2255210
# Joshua Anderson - 2270306
# Eric Vela - 2277759
#
# This class takes in a pandas DataFrame and returns a prediction
#  of a value based on a First Order Markov Model

import numpy as np
import random as rand
import pandas as pd

class FOM:

    # Constructor
    def __init__(self, rows = None):
        if rows == None:
            self.MAX_ROWS = 400000  # Set default to 400k  
        else:
            self.MAX_ROWS = rows    # Set a limit on how many rows are trained
        self.memory = {}            # Dictionary to store data

    # Train train on pandas DataFrame given key and value columns
    def learn(self, dataFrame, columns):
        keyCol = columns[0] # column to be used as keys
        valCol = columns[1] # column to be used as values

        # iterate through every row in DataFrame
        for i, row in enumerate(dataFrame.iterrows()):
            row = row[1] # get row out of tuple from iterrows()

            # Stop training if max rows is reached
            if(i >= self.MAX_ROWS):
                break

            # Add to dictionary
            if row[keyCol] not in self.memory.keys():
                self.memory[row[keyCol]] = []
            self.memory[row[keyCol]].append(row[valCol])

    # Predicts next value given the current value
    def predict(self, category, key):
        data = self.listToDict(self.memory[category]) # get dictionary of all values
        values = data[key]
        count = {}

        # Iterate through each value for the given key
        # and calulate probabilities
        for val in values:
            if val not in count.keys():
                count[val] = 0
            count[val] += 1
        for key in count.keys():
            count[key] = count[key] / len(values)

        # make prediction based on probabilities
        pred = self.choose(count)
        return pred

    # Chooses a value in a given dictionary of probabilities
    def choose(self, dict):
        randVal = rand.random()
        total = 0
        for key, value in dict.items():
            total += value
            if randVal <= total:
                return key

    # Converts a list to a dictionary containing keys of each
    # unique value and lists of "next values"
    def listToDict(self, list):
        dict = {}
        for i, value in enumerate(list):
            if value not in dict.keys():
                dict[value] = []
            try:
                dict[value].append(list[i+1])
            except:
                pass
        return dict

    def getMemory(self):
        return self.memory
