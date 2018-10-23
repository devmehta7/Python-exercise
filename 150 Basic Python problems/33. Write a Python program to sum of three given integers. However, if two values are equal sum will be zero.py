def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
x=int(input("enter any number 1: "))
y=int(input("enter any number 2: "))
z=int(input("enter any number 3: "))
print(sum(x,y,z))
