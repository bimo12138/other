# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:43:58 2019

@author: 13716
"""

import time 

for i in range(1, 100):
    print("\r" + "*" * i, end="")
    time.sleep(1)