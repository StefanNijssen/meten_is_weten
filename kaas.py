a = input("waarde van a")
b = input("waarde van b")

if a > b:
    print("a is het grootste getal")
    max = a
    min = b
elif b > a:
    print("a is het kleinste getal")
    min = a
    max = b
else:
    print("a en b zijn even groot")
print("Het minimum is: " + min)
print("Het maximum is: " + max)