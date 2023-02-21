import sys

input=sys.stdin.readline

# class Node:
#   def __init__(self, data, next=None):
#     self.data = data
#     self.next = next

# class LinkedList:
#   def __init__(self):
#     self.no = 0 # 링크드 리스트의 길이
#     self.head = None # 머리 노드
#     self.current = None
  
#   def __len__(self):
#     return self.no

# if __name__=="__main__":
#   N=input().rstrip()
#   for i in N:

# 파이썬에서 사용되는 리스트는 '배열'로서 구현되어 있다.
# insert나 del을 할때 n번씩 데이터를 밈 - 시간초과
# append(): O(1)
# pop() : O(1)
# insert(): O(N)
# append와 pop만을 이용해 구현해야 한다. stack을 두개로

def linked_list(x):
  global N1,N2
  if x[0]=='L':
    if N1:
      N2.append(N1.pop())
  elif x[0]=='D':
    if N2:
      N1.append(N2.pop())
  elif x[0]=='B':
    if N1:
      N1.pop()
  else:
    N1.append(x[2])

if __name__=="__main__":
  N1=list(input().rstrip())
  N2=[]
  M=int(input())
  for _ in range(M):
    x=input().rstrip()
    linked_list(x)
    
  res=N1+N2[::-1]
  print(''.join(res))