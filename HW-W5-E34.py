numbers_array = []
for n in range(20):
    number = float(input("Please input a number: "))
    numbers_array.append(number)
print("min: ", (min(numbers_array)))
print("max: ", (max(numbers_array)))
print("numbers: ", numbers_array)
print("sum: ", sum(numbers_array))
print("average: ", sum(numbers_array)/len(numbers_array))