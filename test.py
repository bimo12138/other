# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:31:08 2019

@author: 13716
"""

import csv
import random
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, "r")as f:
        lines = csv.reader(f)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random()