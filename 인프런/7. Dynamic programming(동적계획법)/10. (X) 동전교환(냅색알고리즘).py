import sys
# 냅색 알고리즘
if __name__=="__main__":
  input=sys.stdin.readline
  n=int(input())
  coin=list(map(int,input().split())) # 1 2 5
  m=int(input())
  dy=[1000]*(m+1)
  dy[0]=0
  for i in range(n):
    for j in range(coin[i],m+1): # 1~15, 2~15, 5~15
      dy[j]=min(dy[j],dy[j-coin[i]]+1)
  print(dy[m])