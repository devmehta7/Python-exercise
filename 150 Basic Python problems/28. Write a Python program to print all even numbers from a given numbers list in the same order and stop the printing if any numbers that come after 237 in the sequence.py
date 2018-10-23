def is_even(list):
    for n in list:
        if n%2==0 and n<237 :
            print(n)
        if n>237:
            break

is_even([1,2,3,4,5,100,200,300,10,250,210])