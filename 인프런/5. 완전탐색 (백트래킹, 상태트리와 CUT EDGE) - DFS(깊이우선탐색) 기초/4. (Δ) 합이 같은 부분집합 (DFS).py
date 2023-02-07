import sys

# level 개념과 sys.exit(0) 사용해서 다시 풀 것

def DFS(L,sum):
  if sum>total//2: # 속도를 빠르게 (꼭 필요x)
    return # DFS 함수 종료
  if L==n: # 6이 되면 종료
    if sum==(total-sum):
      print("YES")
      sys.exit(0) # 프로그램 종료
  else:
    DFS(L+1, sum+a[L])
    DFS(L+1, sum)
    
if __name__=="__main__":
  n=int(input())
  a=list(map(int,input().split()))
  total=sum(a)
  DFS(0,0)
  print("NO")


# 내 답도 맞음. 하지만 level개념을 사용하지 x
# def DFS(v):
#   if v==(N+1):
#     s1=0
#     s2=0
#     for i in range(1,N+1):
#       if ch[i]==1:
#         s1+=arr[i-1]
#       else:
#         s2+=arr[i-1]
#     if s1==s2:
#       res[0]+=1
         
#   else:
#     ch[v]=1
#     DFS(v+1)
#     ch[v]=0
#     DFS(v+1)

# if __name__=="__main__":
#   input=sys.stdin.readline
#   N=int(input())
#   arr=list(map(int,input().split()))
#   ch=[0]*(N+1)
#   res=[0]
#   DFS(1)
#   if res[0]==0:
#     print("NO")
#   else:
#     print("YES")
  
  