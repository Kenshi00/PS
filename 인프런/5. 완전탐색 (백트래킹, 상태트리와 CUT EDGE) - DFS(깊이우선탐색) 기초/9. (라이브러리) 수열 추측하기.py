import sys
import itertools as it
# itertools -> 순열, 조합 자동으로 구해줌
# 너무 라이브러리에 의존해서는 안됨. 코딩테스트 때 막아 놓는 경우 많음.

input=sys.stdin.readline
N,F=map(int,input().split())
# 이항계수
b=[1]*N # 1 1 1 1
for i in range(1,N):
  b[i]=b[i-1]*(N-i)//i
a=list(range(1,N+1))
for tmp in it.permutations(a): # (a,3) 이면 3개를 뽑아서 만들어줌
  sum=0
  for L, x in enumerate(tmp): # L-index x- value
    sum+=(x*b[L])
  if sum==F:
    for x in tmp: # 튜플도 이렇게 접근 가능하네
      print(x,end=' ')
    sys.exit(0)






# 일단 순열+이항계수로 풀면 이러함
# def DFS(L):
#   if L==N:
#     sum=0
#     for i in range(N):
#       sum+=(res[i]*b[i])
#     if sum==F:
#       for i in res:
#         print(i,end=' ')
#       sys.exit(0)
#   else:
#     for i in range(1,N+1):
#       if ch[i]==0:
#         ch[i]=1
#         res[L]=i
#         DFS(L+1)
#         ch[i]=0

# if __name__=="__main__":
#   input=sys.stdin.readline
#   N,F=map(int,input().split())
#   res=[0]*N
#   ch=[0]*(N+1)
#   b=[1]*N
#   for i in range(1,N):
#     b[i]=b[i-1]*(N-i)//i
#   DFS(0)