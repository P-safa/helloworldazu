
#we get 5 integer inputs from the user
input1 = int(input("please enter a number : "))
input2 = int(input("please enter a second number : "))
input3 = int(input("please enter a third number : "))
input4 = int(input("please enter a forth number : "))
input5 = int(input("please enter a fifth number : "))

if input1 == input2 or input1 == input3 or input1 == input4 or input1 == input5:

    print("Duplicate")
    #we make sure input1 is not repeated
elif input2 == input3 or input2 == input4 or input2 == input5 or input3 == input4 or input3 ==input5 or input4 == input5:
    print("Duplicate")
    #then we check each input 2,3,4,5 is also not repeated
else:
    print("All unique")
    #we have our output