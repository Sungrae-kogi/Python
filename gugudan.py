i=2
j=1
while i<=9 and j<=9:
    print("{} * {} = {}".format(i,j,i*j))
    j=j+1
    if j==10:
        i=i+1
        j=1
        print()
    
