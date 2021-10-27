print("welcome")
a=int(input("enter row: "))
b=int(input("enter column: "))  
for  i in range(a):
        for j in range(b):
            if (i % 2== 0):
               if (j % 2== 0):
                    print("#",end="")
            else: 
                     print("*",end="")
        else:
            if (j % 2== 0):
                     print("*",end="")
else:
            print("#",end="")
            print("")


            
            
                
            
        
    
    










