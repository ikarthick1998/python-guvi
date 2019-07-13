f=int(input())
mult=1
if f==0:
  print(mult)
elif f>0:
  for i in range(1,f+1):
    mult*=i
  print(mult)
