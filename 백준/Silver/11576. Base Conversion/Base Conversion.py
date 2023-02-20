import sys

if __name__=="__main__":
  input=sys.stdin.readline
  A,B=map(int,input().split())
  m=int(input())
  a=list(map(int,input().split()))
  t=''
  for i in a:
    if 0<=i<10:
      t+=str(i)
    else:
      t+=chr(i+55)
  
  t=int(t,A)
  res=[]
  while t!=0:
    res.append(t%B)
    t=t//B
  for i in res[::-1]:
    print(i,end=' ')