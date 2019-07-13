E=int(input())
mult=1
if E==0:
  print(mult)
elif E>0:
  for i in range(1,E+1):
    mult*=i
  print(mult)
