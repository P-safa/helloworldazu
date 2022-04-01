# GET 2 INPUTS

Num1 = int(input("Enter First number :"))
Num2 = int(input("Enter Second number :"))
# 3RD VARIABLE USED FOR GCD
GCD = 0
# GET THE SMALLER NUMBER (IF Num1 == Num2 ==> we print only one of them
if Num1 > Num2:
    GCD = Num2
elif Num2 > Num1:
    GCD = Num1
elif Num2 == Num1:
    print("GCD =", end=" ")
    print(Num2)

# we use this loop to find the biggest divisor
while GCD >= 1:
    if Num1 % GCD == 0 and Num2 % GCD == 0:
        print("GCD =", end=" ")
        print(GCD)
        break
    GCD = GCD - 1

