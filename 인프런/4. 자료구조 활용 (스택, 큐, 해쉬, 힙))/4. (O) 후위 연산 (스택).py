import sys

input=sys.stdin.readline

N=list(input().strip())

def operator(v1,v2,s):
  if s=='+':
    return v1+v2
  elif s=='-':
    return v1-v2
  elif s=='*':
    return v1*v2
  elif s=='/':
    return v1/v2

stack=[]
# isdecimal() - str이 숫자인지 판별
for i in range(len(N)):
  if N[i].isdecimal():
    stack.append(N[i])
  else:
    rt=stack.pop()
    lt=stack.pop()
    tmp=operator(int(lt),int(rt),N[i])
    stack.append(tmp)
print(stack[0])


# while len(N)>1:
#   for i in range(len(N)):
#     # 숫자가 아니면
#     if not N[i].isdecimal():
#       tmp=str(operator(int(N[i-2]),int(N[i-1]),N[i]))
#       N.pop(i-2)
#       N.pop(i-2)
#       N.pop(i-2)
#       N.insert(i-2,tmp)
#       break
# print(N[0])

