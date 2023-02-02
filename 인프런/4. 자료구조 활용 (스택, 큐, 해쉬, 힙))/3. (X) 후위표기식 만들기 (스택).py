import sys
# 문제 이해, 이해 후 구현 둘다 안됐다..
# stack에는 연산기호만 넣는 것
# () 괄호 안에서도 */ , +-의 법칙은 통용되는것! 헷갈x
input=sys.stdin.readline

arr=list(input().strip())
stack=[]
res=""
for i in arr:
  # 숫자가 들어왔을 때
  if '1'<=str(i)<='9':
    res+=str(i)
  # -,+ 일 땐 *,/,-,+ 인 경우에 뺌 ( ( 나오면 멈춤)
  # while stack은 스택이 차있는 경우
  elif i=='-' or i=='+':
    while stack and (stack[-1]!='('):
      res+=stack.pop()
    stack.append(i)
  # *,/ 일 땐 *,/ 인 경우만 뺌
  elif i=='*' or i=='/':
    while stack and (stack[-1]=='*' or stack[-1]=='/'):
      res+=stack.pop()
    stack.append(i)
  # ( 일땐
  elif i=='(':
    stack.append(i)
  # ) 일땐
  elif i==')':
    while stack and stack[-1]!='(':
      res+=stack.pop()
    stack.pop()

while stack:
  res+=stack.pop()
print(res)

    