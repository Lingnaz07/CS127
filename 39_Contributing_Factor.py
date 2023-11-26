#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date November, 7 2023

import pandas as pd


input_file = input("Enter the CSV file name: ")

file = pd.read_csv(input_file)

print(file["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])