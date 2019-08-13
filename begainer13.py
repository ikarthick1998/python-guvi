NU=int(input())
if NU>=0:
    for i in range(2,NU) :
        if NU%i==0:
            print('no')
            break
    else:
        print('yes')
