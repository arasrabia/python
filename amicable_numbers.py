# -*- coding: utf-8 -*-
"""amicable_numbers

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Cy2P0p1c9aMy_fTxO57HoG2rcHtVtSX
"""

x = int(input(''))
y = int(input(''))
sum1 = 0
sum2 = 0
for i in range(1, x):
  if x % i == 0:
    sum1 += i
for j in range(1, y):
  if y % j == 0:
    sum2 += j

if sum1 == j and sum2 == i:
  print('Amicable number')
else:
  print('Not Amicable number')