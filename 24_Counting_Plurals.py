#Name: Lingna Zheng
#Email: LINGNA.ZHENG07@myhunter.cuny.edu
#Date: October,9 2023

wds = input("Enter noun: ")
num = wds.count(" ")+1
print("Number of words: ",num)
numS =wds.count("s ")
if wds[-1] == "s":
    plural = (numS+1)/num
else: 
    plural = numS/num
print("Fraction of your list that is plural is ", plural)