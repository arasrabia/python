# -*- coding: utf-8 -*-
"""Fibonacci numbers

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eLLmJ1JJgaoD92QJPNd_tdPH16BDlKz4
"""

def fibonacci(num):
    ls = [0, 1]
    for i in range(1, num+1):
       i = ls[-1] + ls[-2]
       ls.append(i)
    return ls
          
ls = fibonacci(9)
ls.pop(0)
print(ls)