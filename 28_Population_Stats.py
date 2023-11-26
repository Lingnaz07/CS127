#Name: Lingna Zheng
#Email: LINGNA.ZHENG07@myhunter.cuny.edu
#Date: October,17 2023

import pandas as pd
import matplotlib as plt

place = input('Enter borough: ')
az = pd.read_csv('nycHistPop.csv',skiprows=5)

print(az[place].mean())
print(az[place].max())

