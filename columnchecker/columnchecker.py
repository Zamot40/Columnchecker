# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:41:33 2021

@author: CoolT
"""

import numpy as np
import pandas as pd

class columnchecker:
    def __init__(self, work):
        self.work2 = work
        
        
    def datecheck(self, data):
        shape = np.shape(data)
        for column in range(0,shape[1]):
            for row in range(0,shape[0]):
                if data[row,column].dtype == '<U10' or data[row,column].dtype == 'M':
                    if data[row,column] > '1990-01-01':
                        print("RowNumber:"+ str(row) + " ColumnNumber:" + str(column))
                        
                        
    def oddrows(self, data):
        shape = np.shape(data)
        countINT = 0
        countSTR = 0
        countFLOAT = 0
        countUNI = 0
        for column in range(0, shape[1]):
            for row in range(0, shape[0]):
                if data[row, column].dtype == "i":
                    countINT += 1
                        
                if data[row, column].dtype == "S":
                    countSTR += 1
                        
                if data[row, column].dtype == "f":
                    countFLOAT += 1
                        
                if data[row, column].dtype == "<U10":
                    countUNI += 1
            
            
        print("INT:" + str(countINT) + " STR:" + str(countSTR) +" FLOAT:" + str(countFLOAT)+ " UNI:" + str(countUNI))
        
        for column in range(0, shape[1]):
            for row in range(0, shape[0]):
                if countINT > 0.9*shape[0] and data[row, column].dtype != 'i':
                    print("RowNumber:"+ str(row) + " ColumnNumber:" + str(column))
                
                if countSTR > 0.9*shape[0] and data[row, column].dtype != 'S':
                    print("RowNumber:"+ str(row) + " ColumnNumber:" + str(column))
                
                if countFLOAT > 0.9*shape[0] and data[row, column].dtype != 'f':
                    print("RowNumber:"+ str(row) + " ColumnNumber:" + str(column))
                    
                if countUNI > 0.9*shape[0] and data[row, column].dtype != '<U10':
                    print("RowNumber:"+ str(row) + " ColumnNumber:" + str(column))
                    
#Check if any string of length 10 or datatype datetime is higher than eg. 120 years old. 