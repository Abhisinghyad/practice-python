'''import math
while True:
    num=int(input("Enter the Number: "))
    result=math.factorial(num)
    print("Factorial of",num,"is",result)
    break;
'''
'''num=int(input("Enter the number: "))
fac=1
i=1
while i <=num:
    fac=fac*i
    i=i+1
    print("Factorial",num ,"is",fac)
'''

print("using def function")
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
    
num=int(input("Enter the Number: "))
result=fact(num)
print("Factorial of",num,"is",result)
