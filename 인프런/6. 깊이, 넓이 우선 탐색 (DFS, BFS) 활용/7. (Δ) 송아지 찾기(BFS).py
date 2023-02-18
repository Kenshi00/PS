import sys
from collections import deque
# BFS - level 탐색
# 내 풀이와 다른점은 체크배열로 체크를 해주고, dis[] 거리배열을 만들어서 L을 체크해준 것이 다름


MAX=100000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)
n,m=map(int,input().split())
ch[n]=1
dis[n]=0
dQ=deque()
dQ.append(n)
while dQ:
  now=dQ.popleft()
  if now==m:
    break
  for next in (now-1, now+1, now+5):
    if 0<next<=MAX:
      if ch[next]==0:
        dQ.append(next)
        dis[next]=dis[now]+1
        ch[next]==1
print(dis[m])

# BFS queue를 이용하는 원리는 잘 생각해냈으나 구현이 잘 안됐음 시간초과가 나는데 지금 VSCODE나 채점 프로그램이 이상한 것 같다.
# def DFS(L):
#   global q,E
#   while True:
#     k=len(q)
#     for _ in range(k):
#       tmp=q.popleft()
#       if tmp==E:
#         print(L)
#         sys.exit(0)
#       else:
#         for j in jump:
#           if tmp+j not in q:
#             q.append(tmp+j)
#     L+=1

# if __name__=="__main__":
#   input=sys.stdin.readline
#   S,E=map(int,input().split())
#   jump=[5,1,-1]
#   q=deque()
#   for i in jump:
#     q.append(S+i)
#   DFS(1)