#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date November,26 2023

ADDI $s0, $zero, 10 #set s0 to 10
ADDI $s1, $zero, 5  #use to decrement counter, $s0
ADDI $s2, $zero, 50
AGAIN: ADD $s0, $s0, $s1
BEQ $s0, $s2, DONE
J AGAIN
DONE: