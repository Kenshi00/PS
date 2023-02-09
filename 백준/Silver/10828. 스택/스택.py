import sys

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  stack=[]
  for _ in range(N):
    f=input().rstrip()

    if f=='pop':
      if stack:
        print(stack.pop())
      else:
        print(-1)

    elif f=='size':
      print(len(stack))
    
    elif f=='empty':
      if stack:
        print(0)
      else:
        print(1)
    
    elif f=='top':
      if stack:
        print(stack[-1])
      else:
        print(-1)
    
    else: # push 3
      stack.append(int(f[5:]))

  