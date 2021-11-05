from operator import attrgetter
import random
import pprint
import numpy as np


#inicialization of variables

n = int(input("Enter the number of candidates:\n"))
n = round(n)
if 0>=n  : #this is used to avoid any problems
    while True:
        n = int(input("Please enter a valid value:\n"))
        n = round(n)
        if(0<n):
            break

p = int(input("Enter the value for the facilities to be built (p):\n"))
p = round(p)
if 0>=p  : #this is used to avoid any problems
    while True:
        p = int(input("Please enter a valid value:\n"))
        p = round(p)
        if(0<p):
            break

x_max = int(input("Enter the value of X Max:\n"))
x_max = round(x_max)
if 0>=x_max  : #this is used to avoid any problems
    while True:
        x_max = int(input("Please enter a valid value for X Max:\n"))
        x_max = round(x_max)
        if(0<x_max):
            break
x_min = int(input("Enter the value of X Min:\n"))
x_min = round(x_min)
if x_min>=x_max  or 0>=x_min: 
    while True:
        x_min = int(input("Please enter a valid value for X Min:\n"))
        x_min = round(x_min)
        if(x_min<x_max and 0<x_min):
            break

y_max = int(input("Enter the value of Y Max:\n"))
y_max = round(y_max)
if 0>=y_max  : #this is used to avoid any problems
    while True:
        y_max = int(input("Please enter a valid value for Y Max:\n"))
        y_max = round(y_max)
        if(0<y_max):
            break

y_min = int(input("Enter the value of Y Min:\n"))
y_min = round(y_min)
if y_min>=y_max  or 0>=y_min: 
    while True:
        y_min = int(input("Please enter a valid value for Y Min:\n"))
        y_min = round(y_min)
        if(y_min<y_max and 0<y_min):
            break


k = int(input("Choose how many instances you would like to run:\n"))
k = round(k)
cont=0
if 0>=k  : 
    while True:
        k = int(input("Please enter a valid value:\n"))
        k = round(k)
        if(0<k):
            break

for i in range(k):
    cont=cont+1

#creating the output file
    #file = open("outputfile"+ str(cont) +".txt","w")
    file = open("outputfile2.txt","w")
    file.write(str(n) + " " + str(p) +"\n")

    #for creating the matrix and generating the random numbers
    for i in range(n):
        x = random.randint(x_min,x_max)
        y= random.randint(y_min,y_max)

        file.write("" + str(x) + " ")
        file.write("" + str(y) + "\n")
   
    file.close()
