import sys

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  res=[]
  for _ in range(N):
    a,b,c,d=map(str,input().rstrip().split())
    res.append((a,int(b),int(c),int(d)))
  res.sort(key=lambda x : x[0])
  res.sort(key=lambda x : -x[3])
  res.sort(key=lambda x : x[2])
  res.sort(key=lambda x : -x[1])
  for i in res:
    print(i[0])