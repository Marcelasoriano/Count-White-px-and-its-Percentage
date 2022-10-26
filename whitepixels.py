#Name: Marcela Soriano Cornejo
#Email: marcela.sorianocornejo40@myhunter.cuny.edu
#Date: September 23, 2022
#This program prints counts the percentage of white pixels

import matplotlib.pyplot as plt
import numpy as np

ca = plt.imread(input('Enter file name: '))
countSnow = 0
countPixels = 0
t = float(input('Enter threshold: '))
percent = 0

#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1
          if (ca[i,j,0]<=255):
               countPixels+=1
          
percent = round((countSnow/countPixels)*100,2)
print("number of white pixels: ", countSnow)
print("percent of white pixels: ",str(percent)+"%")