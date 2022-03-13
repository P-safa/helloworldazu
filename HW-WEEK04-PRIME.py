# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


max_val = int(input("enter a celling number(the prime numbers you want up to number) : "))
#questions a bit wierd :)
value = 2

while value <= max_val:
    prime = True
    factor = 2
    while factor < value:
        if value % factor == 0:
            prime = False
            break
        factor += 1
    if prime:
        print(value,end=" ")
    value += 1
print()
##################################################################################################
