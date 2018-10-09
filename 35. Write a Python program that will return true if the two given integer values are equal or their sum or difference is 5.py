def test_number(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

x=int(input("enter any number: "))
y=int(input("enter any number: "))
print(test_number(x,y))