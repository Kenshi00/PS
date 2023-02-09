import sys

if __name__=="__main__":
  input=sys.stdin.readline
  K=int(input())
  stack=[]
  for _ in range(K):
    val=int(input())
    if val==0:
      stack.pop()
    else:
      stack.append(val)
  print(sum(stack))