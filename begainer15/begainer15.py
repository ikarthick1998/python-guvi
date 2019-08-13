NU=int(input())
NU2=int(input())
if NU>0:
    for i in range(NU+1,NU2):
        if i%2==0:
            print(i,end=' ')
else:
    print("enter valied value")
