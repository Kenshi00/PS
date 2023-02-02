import sys

input=sys.stdin.readline

N=list(input().strip())

stack=[]
res=0
for i in N:
  if i=='(':
    stack.append(i)
  elif last=='(':
    stack.pop()
    res+=len(stack)
  else:
    stack.pop()
    res+=1
  last=i
print(res)