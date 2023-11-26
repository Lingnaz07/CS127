#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date October,24 2023

import matplotlib.pyplot as plt
import numpy as np

input_img = input("Enter image file: ")
output_img = input("Enter the output of file: ")

img = plt.imread(input_img)
height = img.shape[0]
width = img.shape[1]
img2 = img[height//2:, :width//2]

plt.imsave(output_img,img2)