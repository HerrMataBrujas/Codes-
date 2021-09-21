# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:29:25 2021

@author: Emilio
"""

#8.4 Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line check
#to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in
#alphabetical order.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "romeo.txt"
fh = open(fname)
lst = list()
#separa las palabras de las lineas y las agrupa en 4 listas, 1xlinea
for line in fh:
    print(line.split())
    #speparar palabras de cada linea; pero solo toma el 1er caracter
    for word in line:
        if not word in lst:
            lst.append(word)
        continue
print(lst)
