#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date November, 6 2023

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = " "
     month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

     monthString = month[monthNum-1]

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################

     return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()