#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date October,27 2023

import pandas as pd
import matplotlib.pyplot as plt


file_name = input("Enter the file name: ")
attribute = input("Enter attribute: ")
file = pd.read_csv(file_name)


print("The 10 worst offenders are: ")
print(file[attribute].value_counts()[:10])

