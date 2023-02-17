import sys

def DFS(L,A,B,C):
  global answer
  if L==N:
    if A!=B and B!=C and A!=C:
      tmp=max(A,B,C)-min(A,B,C)
      answer=min(answer,tmp)
  else:
    # A,B,C 대신 money[]로 만들어서 for문으로 해도 된다.
    DFS(L+1,A+coin[L],B,C)
    DFS(L+1,A,B+coin[L],C)
    DFS(L+1,A,B,C+coin[L])
if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  coin=[]
  for i in range(N):
    coin.append(int(input()))
  answer=214700000
  DFS(0,0,0,0)
  print(answer)