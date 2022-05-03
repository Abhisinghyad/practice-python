#Even Number

#taking Input from user
num=int(input("Enter the Number: "))
'''if num%2==0:
    print("This number is Even: ",num)
elif num%2!=0:
    print("This number is Odd: ",num)
else:
    print("Invalid Number")'''


def findeven(num):
    if num%2==0:
        print("This is a Even number: ",num)
    else:
        print("This is Odd Number: ", num)
findeven(num)