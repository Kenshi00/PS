
# 양 끝단에서 접근하는 lt, rt 개념, 리스트 자료구조 특징 pop(), pop(0)
# a[-1] = a 리스트의 마지막 요소
# deque를 사용하면 pop(0)을 할 때 한 칸 씩 안땡겨도 됨

import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
a=deque(a)
# exit_code_1 나는 이유 : 만약 리스트에 한 사람만 남게되면 a[0]+a[-1] = 한 사람을 두번 더하게 되어버림.
cnt=0
while a: # a 자료구조가 비어있으면 멈춤!
  if len(a)==1:
    cnt+=1
    break
  if a[0]+a[-1]<=M:
    a.popleft()
    a.pop()
  else:
    a.pop()
  cnt+=1

print(cnt)

