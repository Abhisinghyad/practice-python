num=int(input("Enter the Number to find Even or Odd: "))   #taking input from user

def findeven(num):       #function Define
    if num%2==0:    #condition
        print("This is a Even number: ",num)
    else:
        print("This is Odd Number: ", num)
findeven(num)