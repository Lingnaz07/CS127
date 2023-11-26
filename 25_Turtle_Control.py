#Name: Lingna Zheng
#Email: LINGNA.ZHENG07@myhunter.cuny.edu
#Date: October,12 2023

import turtle
az = turtle.Turtle()

commands = input('Enter the commands: ')
for i in commands:
    if i == 'F':
        az.forward(50)
    elif i == 'L':
        az.left(90)
    elif i == 'R':
        az.right(90)
    elif i == '^':
        az.penup()
    elif i == 'v':
        az.pendown()
    elif i == 'B':
        az.backward(50)
    elif i == 'S':
        az.stamp()
    elif i == 'l' :
        az.left(45)
    elif i == 'r' :
        az.right(45)
    elif i == 'p' :
        az.color('purple')
    else:
        print("Error",i)