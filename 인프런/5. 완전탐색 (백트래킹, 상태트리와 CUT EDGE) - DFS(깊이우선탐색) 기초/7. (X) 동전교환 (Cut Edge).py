import sys
# sum값 말고도 Level로 조건을 걸어서 cut edge 할 수 있음
def DFS(L,sum):
  global res
  if res<L:
    return
  if sum==M:
    if L<res:
      res=L
  if sum>M:
    return
  else:
    for i in range(len(a)):
      DFS(L+1,sum+a[i])

if __name__=="__main__":
  N=int(input())
  a=list(map(int,input().split()))
  a.sort(reverse=True)
  M=int(input())
  res=2147000000
  DFS(0,0) # level과 sum
  print(res)



# 내 풀이도 되긴 되는데 너무 오래걸림
# def DFS(L):
#   global answer
#   if sum(res)==M:
#     answer=min(answer,L)
#   if sum(res)>M: # 합이 M 넘어가면 자름
#     return
#   else:
#     for i in a: # 5,2,1
#       res.append(i)
#       DFS(L+1)
#       res.pop()

# if __name__=="__main__":
#   N=int(input())
#   a=list(map(int,input().split()))
#   a.sort(reverse=True)
#   M=int(input())
#   res=[]
#   answer=2147000000
#   DFS(0)
#   print(answer)