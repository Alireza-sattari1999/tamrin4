rows=10 
columns=10  
for i in range(1,rows+1):
    for j in range(1,columns+1):
        c=i*j
        print("{:2d} ".format(c),end='')
    print("\n") 