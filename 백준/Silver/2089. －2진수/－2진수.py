import sys

N=int(input())
res=''
if N==0:
  print(0)
  sys.exit()
while N!=0:
  if abs(N)%2==1: # N이 홀수면
    N=(N-1)//-2
    res+='1'
  else:
    N=N//-2
    res+='0'
print(res[::-1])