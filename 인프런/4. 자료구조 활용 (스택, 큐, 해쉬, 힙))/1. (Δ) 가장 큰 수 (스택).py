import sys

# stack 활용, stack[:-m], ''.join(x for x in stack)
# 이런 기능들 잘 몰랐음.
n,m=map(str,input().split())

stack=[]
arr=list(n)
m=int(m)
for i in range(0,len(arr)):
  while m>0 and stack and arr[i]>stack[-1]:
    stack.pop()
    m-=1
  stack.append(arr[i])

for i in range(m):
  stack.pop()
# if m!=0:
#   stack=stack[:-m]
# print(stack)
print(''.join(x for x in stack))


  
# 내 풀이도 맞음
# a=list(n)
# m=int(m)
# for _ in range(m):
#   max=0
#   for i in range(len(a)):
#     tmp=a[i]
#     del a[i]
#     result=int(''.join(x for x in a))
#     if result>max:
#       max=result
#       index=i
#     a.insert(i,tmp)
#   del a[index]

# print(int(''.join(x for x in a)))