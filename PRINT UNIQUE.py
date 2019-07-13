I=int(input())
C=list(map(int,input().split()))
p=0
d=[]
for i in range(0,I+1):
    if(C.count(i)>1):
      d.append(i)
if(len(d)==0):
    print("unique")
I=sorted(d)
print(' '.join(map(str,I)))
