#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date November, 8 2023

def computeFare(zone, ticketType):
   fare = 0  
   if ticketType == "peak":
        if zone == 1:
            fare = 8.75
        elif zone == 2 or zone == 3:
            fare = 10.25
        elif zone == 4:
            fare = 12.00
        elif zone == 5 or zone == 6 or zone == 7:
            fare = 13.50
        else:
            fare = -1
        
   elif ticketType == "off-peak":
        if zone == 1:
            fare = 6.25
        elif zone == 2 or zone == 3:
            fare = 7.50
        elif zone == 4:
            fare = 8.75
        elif zone == 5 or zone == 6 or zone == 7:
            fare == 9.75
        else:
            fare = -1
   return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()