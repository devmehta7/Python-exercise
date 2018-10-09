def copies(string,n):
    result=""
    length=len(string)
    if length<2:
        for i in range(n):
            result=result+string
        return result
    else:
        string=string[:2]
        for i in range(n):
            result=result+string
        return result


string=input("enter the string: ")
n=int(input("enter the number of copies: "))
print(copies(string,n))
