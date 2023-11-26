#Name: Lingna Zheng
#Email: LINGNA.ZHENG07@myhunter.cuny.edu
#Date: October,14 2023

import matplotlib.pyplot as plt
import pandas as pd



place = input('Enter a place: ')
file = input('Enter the file name: ')
az = pd.read_csv('nycHistPop.csv',skiprows=5)

az['Fraction'] =az[place] / az['Total']

az.plot(x = 'Year',y = 'Fraction')

fig = plt.gcf()
fig.savefig(file)
