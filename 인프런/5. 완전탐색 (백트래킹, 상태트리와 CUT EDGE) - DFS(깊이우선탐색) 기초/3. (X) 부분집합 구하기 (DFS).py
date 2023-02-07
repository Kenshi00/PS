import sys
# O X로 뻗어나가는 트리를 상태트리 라고함
# D(1) - D(2) D(2) - D(3) D(3) D(3)
# 이 개념을 까먹었고, 알고도 구현이 힘들었음
def DFS(v):
  if v==N+1:
    for i in range(1,N+1): # 1 2 3
      if ch[i]==1:
        print(i,end=' ')
    print()
  else:
    ch[v]=1
    DFS(v+1)
    ch[v]=0
    DFS(v+1)
    

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  ch=[0]*(N+1) # 체크배열 활용
  DFS(1)