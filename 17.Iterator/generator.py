def MyGenerater(n):
    index=0
    while index<n:
        yield index**2
        index+=1

if __name__=="__main__":
    x_square=MyGenerater(10)
    for x in x_square:
        print(x)
