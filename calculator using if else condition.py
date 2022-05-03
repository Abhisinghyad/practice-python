num1=int(input("Enter the 1st Number: "))
opr=(input("Select Operator(+,-,*,/):  "))
num2=int(input("Enter the 2nd Number: "))

if opr=="+":
    Sum=(num1+num2)
    print("Sum of the Number: ",Sum)
elif opr=="-":
    sub= (num1-num2)
    print("Subtraction of two Number: ",sub)
elif opr=="*":
    multi=(num1*num2)
    print("multiplication of two Number: ",multi)
elif opr=="/":
    div=(num1/num2)
    print("Division of two Number: ",div)
else:
    print("Invalid Input")
