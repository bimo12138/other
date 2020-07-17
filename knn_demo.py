# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:38:19 2019

@author: 13716
"""

# =============================================================================
# from sklearn import datasets
# from sklearn.cross_validation import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
#  
#  
# iris = datasets.load_iris()
# iris_X = iris.data
# iris_y = iris.target
# print('-----data input example like this -----')
# print(iris_X[:3, :])
# print('------lables like this -------')
# print(iris_y)
#  
#  
# X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
#  
#  
# knn = KNeighborsClassifier()
# knn.fit(X_train, y_train)
# y_predict = knn.predict(X_test)
# print('-----predict value is ------')
# print(y_predict)
# print('-----actual value is -------')
# print(y_test)
# count = 0
# for i in range(len(y_predict)):
#     if y_predict[i] == y_test[i]:
#         count += 1
# print('accuracy is %0.2f%%'%(100*count/len(y_predict)))
# =============================================================================




## KNN DEMO



#!/usr/bin/python
# coding=utf-8
#########################################
# kNN: k Nearest Neighbors
 
#  输入:      newInput:  (1xN)的待分类向量
#             dataSet:   (NxM)的训练数据集
#             labels:     训练数据集的类别标签向量
#             k:         近邻数
 
# 输出:     可能性最大的分类标签
#########################################
 
import numpy as np
from matplotlib import pyplot as plt
 
# 创建一个数据集，包含2个类别共4个样本
def createDataSet():
    # 生成一个矩阵，每行表示一个样本
    group = np.array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    # 4个样本分别所属的类别
    labels = ['A', 'A', 'B', 'B']

    return group, labels

# KNN分类算法函数定义
def kNNClassify(newInput, dataSet, labels, k):
    
    numSamples = dataSet.shape[0]   # shape[0]表示行数
 
    # # step 1: 计算距离[
    # 假如：
    # Newinput：[1,0,2]
    # Dataset:
    # [1,0,1]
    # [2,1,3]
    # [1,0,2]
    # 计算过程即为：
    # 1、求差
    # [1,0,1]       [1,0,2]
    # [2,1,3]   --   [1,0,2]
    # [1,0,2]       [1,0,2]
    # =
    # [0,0,-1]
    # [1,1,1]
    # [0,0,-1]
    # 2、对差值平方
    # [0,0,1]
    # [1,1,1]
    # [0,0,1]
    # 3、将平方后的差值累加
    # [1]
    # [3]
    # [1]
    # 4、将上一步骤的值求开方，即得距离
    # [1]
    # [1.73]
    # [1]
    #
    # ]
    # tile(A, reps): 构造一个矩阵，通过A重复reps次得到
    # tile函数位于python模块 numpy.lib.shape_base中，他的功能是重复某个数组。
    # 比如tile(A,n)，功能是将数组A重复n次，构成一个新的数组
    # the following copy numSamples rows for dataSet
    diff = np.tile(newInput, (numSamples, 1)) - dataSet  # 按元素求差值
    squaredDiff = diff ** 2  # 将差值平方
    squaredDist = sum(squaredDiff, axis = 1)   # 按行累加
    distance = squaredDist ** 0.5  # 将差值平方和求开方，即得距离
    #print(distance)
    # # step 2: 对距离排序
    # argsort() 返回排序后的索引值 数组值从小到大的索引值
    sortedDistIndices = np.argsort(distance)
    #print( sortedDistIndices)
    classCount = {} # define a dictionary (can be append element)
    #print(classCount)
    for i in range(k):
        # # step 3: 选择k个最近邻
        voteLabel = labels[sortedDistIndices[i]]
        #print(voteLabel)
        # # step 4: 计算k个最近邻中各类别出现的次数
        # when the key voteLabel is not in dictionary classCount, get()
        # will return 0
        # classCount.get(voteIlabel,0)返回字典classCount中voteIlabel元素对应的值,若无，则进行初始化
        # 当字典中有voteIlabel元素时，classCount.get(voteIlabel,0)作用是返回该元素对应的值，即0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
        #print(classCount[voteLabel])
    # # step 5: 返回出现次数最多的类别标签
    # 遍历字典列表classCount
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key
 
    return maxIndex


# 生成数据集和类别标签
dataSet, labels = createDataSet()
# 定义一个未知类别的数据
testX = np.array([1.2, 1.0])
k = 3
# 调用分类函数对未知数据分类
outputLabel = kNNClassify(testX, dataSet, labels, 3)
print("Your input is:", testX, "and classified to class: ", outputLabel)
 
testX = np.array([0.1, 0.3])
outputLabel = kNNClassify(testX, dataSet, labels, 3)
print("Your input is:", testX, "and classified to class: ", outputLabel)
 
 