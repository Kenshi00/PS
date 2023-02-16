import sys
# 중복이 안돼야 한다고 해서 꼭 중복순열 같은걸 생각할 필욘 없다. 알맞은 상태트리를 만들어 주면 되는 것
def DFS(L,sum):
  global cnt
  if sum>T:
    return
  if L==k:
    if sum==T:
      cnt+=1
  else:
    for i in range(n[L]+1):
      DFS(L+1,sum+p[L]*i)

if __name__=="__main__":
  input=sys.stdin.readline
  T=int(input())
  k=int(input())
  p=[]
  n=[]
  for i in range(k):
    a,b=map(int,input().split())
    p.append(a)
    n.append(b)
  cnt=0
  DFS(0,0)
  print(cnt)