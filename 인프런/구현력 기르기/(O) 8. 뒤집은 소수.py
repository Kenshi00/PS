import sys

input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))

def reverse(x):
  newNum=0
  while x>0:
    newNum=newNum*10+x%10 # res=res*10+t
    x=x//10
  return newNum

def isPrime(x): # 23
  if x==1: # 1은 항상 소수가 아닌 것 까먹으면 안됨!
    return False
  for i in range(2,x//2+1): # 2~22 == 2~12
    if x%i==0:
      return False
  return True

res=[]
for i in arr:
  res.append(reverse(i))

for i in res:
  if isPrime(i):
    print(i,end=' ')
