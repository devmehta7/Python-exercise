sum=0
num =(input("Input any number: "))
list=[]
for i in range(len(num)):
    list.append(num[i])
print(list)

for i in list:
    sum=sum+int(i)
print("sum of all digit in number: %d"%sum)
