import sys

if __name__=="__main__":
  input=sys.stdin.readline
  T=int(input())
  for _ in range(T):
    N=input().rstrip()
    stack=[]
    answer="YES"
    for i in N: # 한번 돌 때
      if i=='(':
        stack.append(i)
      else:
        if stack:
          stack.pop()
        else: # 스택이 비었는데 닫힌 괄호 만난 경우
          answer="NO"
          break
    
    if stack:
      answer="NO"
    
    print(answer)