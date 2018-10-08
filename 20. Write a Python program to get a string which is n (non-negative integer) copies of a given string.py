
def larger_string(str,n):
    result=""
    for i in range(n):
        result = result + str
    return result

print(larger_string('dev', 2))
print(larger_string('.py', 3))
