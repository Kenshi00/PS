import sys
# 부분집합 사용 - -4가 나오면 4가 무조건 나오는 대칭 속성
# set을 사용하는 이유는 중복이 안돼서
def DFS(L,sum):
  global S
  if L==K:
    if 0<sum<=S:
      res.add(sum)
  else:
    DFS(L+1,sum+a[L])
    DFS(L+1,sum-a[L])
    DFS(L+1,sum)
  

if __name__=="__main__":
  input=sys.stdin.readline
  K=int(input())
  a=list(map(int,input().split()))
  S=sum(a)
  res=set()
  DFS(0,0)
  print(S-len(res))
