import sys

def q(x):
  if x =='pop':
    if queue:
      print(queue.pop(0))
    else:
      print(-1)

  elif x == 'size':
    print(len(queue))
  
  elif x == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  
  elif x == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  
  elif x == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)
  
  else:
    queue.append(int(x[5:]))
if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  queue=[]
  for i in range(N):
    tmp=input().rstrip()
    q(tmp)