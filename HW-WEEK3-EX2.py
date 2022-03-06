
firstNum = int(input("Please enter a number : "))
secondNum = int(input("Please enter another number : "))
thirdNum = int(input("Please enter one more number : "))
#FIRST LETS CHECK IF YOUR INPUTS ARE CORRECT AND MAKE A TRIANGLE
#THEN CHECK IF THE TRIANGLE IS RIGHT!!!
if firstNum + secondNum < thirdNum or firstNum + thirdNum < secondNum or secondNum + thirdNum < firstNum:
    print("error : not a triangle")
else:
    case1 = ((firstNum ** 2) + (secondNum ** 2)) - (thirdNum ** 2)
    case2 = ((firstNum ** 2) + (thirdNum ** 2)) - (secondNum ** 2)
    case3 = ((thirdNum ** 2) + (secondNum ** 2)) - (firstNum ** 2)

    if case1 == 0 or case2 == 0 or case3 == 0:
        print("right")
    else:
        print("not right")