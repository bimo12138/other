# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:50:46 2019

@author: 13716
"""

import os
import sys   
sys.setrecursionlimit(100000) #例如这里设置为十万  
try:
    import rawpy
    import imageio
    import matplotlib.pylab as plt
    from time import sleep
except:
    os.system("pip install rawpy")
    os.system("pip install matplotlib")

def change(filename, basename):
    raw = rawpy.imread(filename)
    rgb = raw.postprocess()
    imageio.imsave('{}.jpg'.format(basename), rgb)
    
    
def list_all_files(file_path):
    return [f for f in os.listdir(file_path)if os.path.isfile(os.path.join(file_path, f))]

if __name__ == "__main__":
    n = 0
    path = input("请输入CR2文件的路径：")
    for file in list_all_files(path):
        filename, ext = os.path.splitext(file)
        if ext.lower() == ".cr2":
            change(filename+ext, filename)
            print(filename + "转化成功！")
            n += 1
    print(str(n) + "个 CR2 文件转化成功！")
    sleep(2)