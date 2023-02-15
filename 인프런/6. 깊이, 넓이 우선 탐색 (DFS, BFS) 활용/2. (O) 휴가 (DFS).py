import sys
# 부분집합 활용
def DFS(L,sum):
  global answer
  if L>N:
    return
  if L==N:
    answer=max(answer,sum)
  else:
    DFS(L+T[L],sum+P[L]) # 상담 o
    DFS(L+1,sum) # 상담 x
if __name__=="__main__":
  N=int(input())
  T=[]
  P=[]
  for _ in range(N):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)
  answer=0
  DFS(0,0)
  print(answer)