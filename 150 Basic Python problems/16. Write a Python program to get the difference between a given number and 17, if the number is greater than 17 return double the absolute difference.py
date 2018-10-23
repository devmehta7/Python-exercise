n=int(input("Enter any number: "))
if (n <= 17):
    diff=17 - n
    print("value is less than 17 so difference is :{0}".format(diff))
else:
    diff=(n - 17) * 2
    print("value is greater than 17 so difference is doubled :{0}".format(diff))
