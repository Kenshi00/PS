import sys

input=sys.stdin.readline

N=int(input())
arr=list(map(int, input().split()))

def digit_sum(x):
  sum=0
  while x!=0:
    sum+=x%10
    x=x//10
  return sum

res=[]
for i in arr:
  res.append(digit_sum(i))
print(arr[res.index(max(res))])

