# -*- coding: utf-8 -*-
"""Calculate letters

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16oBOgiT2P7lG-ckQVqFhC74Tc4XiLEQI
"""

sentences = input('write a sentense: ')
new_list = list(sentences)
new_dict = {}
for i in new_list:
  j = new_list.count(i)
  if j > 0:
    new_dict[i] = j
  
print(dict(new_dict.items()))