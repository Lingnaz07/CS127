#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date October,20 2023

import pandas as pd
import matplotlib.pyplot as plt


input_file = input('Enter a file: ')
output_file = input('Enter the output file: ')

az = pd.read_csv(input_file)
az['Fraction Children'] = az['Total Children in Shelter'] / az['Total Individuals in Shelter']

az.plot(x = 'Date of Census',y = 'Fraction Children' )

fig = plt.gcf()
fig.savefig(output_file)