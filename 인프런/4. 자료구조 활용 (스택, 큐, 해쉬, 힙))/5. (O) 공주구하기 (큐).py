import sys
from collections import deque

input=sys.stdin.readline

N,K=map(int,input().split())

dq = deque([])
for i in range(1,N+1):
  dq.append(i)
# dq=deque(list(range(1,n+1)))
cnt=1
while len(dq)>1:
  if cnt==K:
    dq.popleft()
    cnt=1
  else:
    dq.append(dq.popleft())
    cnt+=1
print(dq[0])
# while len(queue)>1:
#   if i>=len(queue):
#     i=0
#   if cnt==K:
#     queue.pop(i)
#     cnt=1
#   else:
#     i+=1
#     cnt+=1
# print(queue[0])