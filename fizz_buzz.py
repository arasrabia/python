# -*- coding: utf-8 -*-
"""Fizz Buzz

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16oBOgiT2P7lG-ckQVqFhC74Tc4XiLEQI
"""

number = int(input(''))

for i in range(1, 101):
  if i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  elif i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  else:
    print(i)