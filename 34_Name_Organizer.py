#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date October,24 2023


names = input("Enter names: ")
names = names.split(";")

for names in names:
    a = names.split(",") #split names by ,
    print(a[::-1]) # print the last , first name
