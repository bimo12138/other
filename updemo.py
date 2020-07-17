# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:36:57 2019

@author: 13716
"""

import numpy as np
from matplotlib import pyplot as plt

class Application(object):
    
    def __init__(self):
        self.x = [1, 2, 3, 4, 5]
        self.y = [1, 3, 2, 3, 5]
        self.avg_x = sum(self.x)/len(self.x)
        self.avg_y = sum(self.y)/len(self.y)
        self.sum_top = 0
        self.sum_button = 0
        self.x_2 = np.linspace(0.01, 0.6, 60)
        self.init()
        self.get_a_b()
        
    def init(self):
        if len(self.x) == len(self.y):
            for i in range(len(self.x)):
                self.sum_top = ((self.x[i] - self.avg_x) * (self.y[i] - self.avg_y))
                self.sum_button = (self.x[i] - self.avg_x) ** 2
        else:
            print("两个数组长度不一致, 无法计算!")
            
    def get_a_b(self):
        
        self.a = self.sum_top / self.sum_button
        self.b = self.avg_y - self.a * self.avg_x
    
    def get_answer_one(self):
        plt.scatter(self.x, self.y)
        plt.show()
    
    def func(self, x_2):
        return self.a * x_2 + self.b
    
    def get_answer_two(self):
        plt.plot(self.x_2,  self.func(self.x_2), "r-", linewidth=1, label="(2)")
        plt.show()
        
if __name__ == "__main__":
    app = Application()
    app.get_answer_one()
    app.get_answer_two()