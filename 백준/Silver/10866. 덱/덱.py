import sys
from collections import deque
# deque (stack, queue 둘다 됨)
# stack -> append(), pop()
# queue -> appendleft(), popleft(), append(), pop()
# insert(), remove()

def Deque(x):
  if 'push_front' in x:
    dq.appendleft(int(x[11:]))
  
  elif 'push_back' in x:
    dq.append(int(x[10:]))
  
  elif x == 'pop_front':
    if dq:
      print(dq.popleft())
    else:
      print(-1)
  
  elif x == 'pop_back':
    if dq:
      print(dq.pop())
    else:
      print(-1)
  
  elif x == 'size':
    print(len(dq))
  
  elif x == 'empty':
    if dq:
      print(0)
    else:
      print(1)
  
  elif x == 'front':
    if dq:
      print(dq[0])
    else:
      print(-1)
  
  elif x == 'back':
    if dq:
      print(dq[-1])
    else:
      print(-1)

if __name__=="__main__":
  input=sys.stdin.readline
  dq=deque()
  N=int(input())
  for i in range(N):
    tmp=input().rstrip()
    Deque(tmp)