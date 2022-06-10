n=10

for i in range(10):
     print(" " * (n-i-1),end=" ")
     print("*" * (2*i+1),end=" ")
     print(" " * (n-i-1))

n=6
for i in range(6):
    if (i==0 or i==(n-1)):
        print("*" * n)
        
    
