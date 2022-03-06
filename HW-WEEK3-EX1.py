
income = int(input("How much is your incom ? "))

if 0 < income < 1000:
    afterReduction = income
    print("income after tax is", end=" $")
    print(afterReduction)
elif 1000 < income <= 2500:
    afterReduction = income - (income * 0.1)
    print("income after tax is", end=" $")
    print(afterReduction)
elif 2500 < income <= 4000:
    afterReduction = income - (income * 0.15)
    print("income after tax is", end=" $")
    print(afterReduction)
elif 4000 < income <= 6000:
    afterReduction = income - (income * 0.2)
    print("income after tax is", end=" $")
    print(afterReduction)
elif 6000 < income <= 8000:
    afterReduction = income - (income * 0.25)
    print("income after tax is", end=" $")
    print(afterReduction)
elif income < 8000:
    afterReduction = income - (income * 0.3)
    print("income after tax is", end=" $")
    print(afterReduction)
else:
    print("ERROR ((either your input is higher than this programs range or ...))")
