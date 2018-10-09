def sum(n1,n2):
    sum=int(n1+n2)
    if sum<20 and sum>15:
        sum=20
    return sum


n1=int(input("enter any number: "))
n2=int(input("enter any number: "))
print(sum(n1,n2))