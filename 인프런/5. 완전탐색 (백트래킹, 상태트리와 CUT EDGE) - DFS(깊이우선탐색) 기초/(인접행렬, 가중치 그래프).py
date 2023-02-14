import sys

if __name__=="__main__":
  N,M=map(int,input().split())
  a=[[0]*(N+1) for _ in range(N+1)]
  for _ in range(M):
    n1,n2,n3 = map(int,input().split())
    a[n1][n2]=n3
    # 무방향 그래프는 a[n2][n1]=n3 한번 더 해주면 됨
  for i in range(1,N+1):
    for j in range(1,N+1):
      print(a[i][j],end=' ')
    print()