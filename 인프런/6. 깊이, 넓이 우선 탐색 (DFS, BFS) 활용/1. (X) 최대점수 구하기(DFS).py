import sys
# 부분집합 활용
def DFS(L,sum,n):
  global answer
  if sum>M:
    return
  if L==N:
    answer=max(answer,n)
  else:
    DFS(L+1,sum+time[L],n+score[L])
    DFS(L+1,sum,n)

if __name__=="__main__":
  input=sys.stdin.readline
  N,M=map(int,input().split())
  score=[0]*N
  time=[0]*N
  for i in range(N):
    score[i],time[i]=map(int,input().split())
  answer=0
  DFS(0,0,0)
  print(answer)


# 시간 초과, 그리고 방식을 다르게 접근함
# def DFS(cnt,sum):
#   global answer
#   if sum>M:
#     return
#   else:
#     for i in range(N):# 0~4
#       if ch[i]==0:
#         ch[i]=1
#         DFS(cnt+score[i],sum+time[i])
#         answer=max(answer,cnt)
#         ch[i]=0


# if __name__=="__main__":
#   input=sys.stdin.readline
#   N,M=map(int,input().split())
#   score=[]
#   time=[]
#   for i in range(N):
#     a,b=map(int,input().split())
#     score.append(a)
#     time.append(b)
#   ch=[0]*N
#   answer=0
#   DFS(0,0)
#   print(answer)