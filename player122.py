a,b=map(int,input().split())
li=list(map(int,input().split()[:a]))
for i in range(0,b):
    li=[li[-1]]+li[:-1]
for j in li:
    print(j,end=" ")
        
    
