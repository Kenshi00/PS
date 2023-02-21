import sys

if __name__=="__main__":
  input=sys.stdin.readline
  N,K=map(int,input().split())
  a=list(map(int,input().split()))
  a.sort()
  print(a[K-1])
  