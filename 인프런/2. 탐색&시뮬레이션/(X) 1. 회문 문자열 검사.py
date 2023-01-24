import sys

# sys.stdin.readline은 문자열을 입력받을 때 strip()을 써줘야 하는걸 깜빡했고, list.reverse() 말고 tmp[::-1] 방법이 있음을 알게 되었음

input=sys.stdin.readline

N=int(input())

for i in range(N):
  tmp=input().strip()
  tmp=tmp.upper()

  if tmp==tmp[::-1]:
    print("#%d YES" %(i+1))
  else:
    print("#%s NO" %(i+1))



