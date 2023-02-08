import sys
# Cut Edge Tech
# 시간 초과로 인해 틀림 - tsum 조건 추가해야함.
# tsum은 지금 레벨에서 최대의 sum 값
# sum+(total-tsum), 즉, 현재의 값에(sum) 앞으로 가능한 최대의 값(total-tsum)의 합이 이미 저장되어 있는 res보다 작으면 return

def DFS(L,sum,tsum):
  global res
  if res>=sum+(total-tsum):
    return
  if sum>C:
    return
  if L==N:
    if sum<=C:
      res=max(sum,res)
      return
  else:
    DFS(L+1,sum+a[L],tsum+a[L])
    DFS(L+1,sum,tsum+a[L])

if __name__=="__main__":
  input=sys.stdin.readline
  C,N=map(int,input().split())
  a=[]
  for i in range(N):
    a.append(int(input()))
  total=sum(a)
  res=0
  DFS(0,0,0)
  print(res)