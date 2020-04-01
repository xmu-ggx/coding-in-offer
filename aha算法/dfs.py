# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:37:54 2020

@author: GGX
"""

# 输出1~n的全排列(深度优先搜索)
class Solution():
    def __init__(self, x):
        self.n = x
        self.book = [1 for _ in range(x)]
        self.res = [-1 for _ in range(x)]
        
    def fun(self, step):
        
        if step == self.n:
            print(self.res)
            return
        
        for i in range(self.n):
            if self.book[i] == 1:
                self.res[step] = i+1
                self.book[i] = 0
                self.fun(step+1)
                self.book[i] = 1  #
        
        
Solution(4).fun(0)
