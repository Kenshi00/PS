import sys
# 일단 1234, 1243.. 등 중복 순열 이용
# 파스칼 규칙 - 이항계수
# (a+b)^2 -> 1 2 1
# (a+b)^3 -> 1 3 3 1
# (a+b)^4 -> 1 4 6 4 1 == 4C0 4C1 4C2 4C3 4C4
def DFS(L):
  global b
  if L==N:
    sum=0
    for i in range(N):
      sum+=(res[i]*b[i])
    if sum==F:
      for i in range(N):
        print(res[i],end=' ')
      print()
      sys.exit(0)
    
  # global answer
  # if L==N:
  #   # Paskal - 내가 한 건 매번 while 돌아야 해서 비효율
  #   answer=res.copy()
  #   while len(answer)>1:
  #     tmp=answer.copy()
  #     answer.clear()
  #     for i in range(len(tmp)-1):
  #       answer.append(tmp[i]+tmp[i+1])
    # if answer[0]==F:
    #   for i in range(N):
    #     print(res[i], end=' ')
    #   print()
    #   sys.exit(0)
  else:
    for i in range(1,N+1):
      if ch[i]==0:
        ch[i]=1
        res[L]=i
        DFS(L+1)
        ch[i]=0

if __name__=="__main__":
  input=sys.stdin.readline
  N,F=map(int,input().split())
  b=[1]*N
  res=[0]*N
  ch=[0]*(N+1)
  for i in range(1,N): # 이항계수(조합)
    b[i]=b[i-1]*(N-i)//i
  DFS(0)