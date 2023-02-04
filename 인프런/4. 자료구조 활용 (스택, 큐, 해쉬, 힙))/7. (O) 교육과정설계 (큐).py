import sys
from collections import deque
input=sys.stdin.readline

M=deque(list(input().strip()))
N=int(input())

for i in range(N):
  dq=deque(list(input().strip()))
  tmp=M.copy()
  for j in dq:
    if j in tmp:
      if j==tmp[0]:
        tmp.popleft()
      else: # 커리큘럼 순서가 꼬인 경우
        break
  if not tmp:
    print('#'+str(i+1)+' YES')
  else:
    print('#'+str(i+1)+' NO')

