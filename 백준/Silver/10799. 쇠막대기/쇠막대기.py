import sys

if __name__=="__main__":
  input=sys.stdin.readline
  N=input().rstrip()
  stack=[]
  answer=0
  tmp=''
  for i in N:
    if i=='(':
      stack.append('(')
      answer+=1
    else: # 닫힌 괄호가 나온 경우
      stack.pop()
      if tmp=='(':
        answer-=1
        answer+=len(stack)
    tmp=i
  
  print(answer)
