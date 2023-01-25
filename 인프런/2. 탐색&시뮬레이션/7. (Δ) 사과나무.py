import sys

input=sys.stdin.readline

N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]

res=0
s=e=N//2
for i in range(N):
  res+=sum(a[i][s:e+1]) # 밑이랑 같은 말!
  # for j in range(s, e+1):
  #   res+=a[i][j]
  if i<N//2:
    s-=1
    e+=1
  else:
    s+=1
    e-=1

print(res)
# 내 풀이 (매우 어렵게 품)
# tmp=1
# s=0
# key=[]
# for i in range(N):
#   s=i+tmp
#   tmp+=1
#   if s<=N:
#     key.append(s)
#   else:
#     key.append(2*N-s)

# res=0
# for i in range(len(key)): # key[1,3,5,3,1]
#   x=(N-key[i])//2  # 2 1 0 1 2
#   res+=sum(a[i][x:x+key[i]]) # a[0][2:3], a[1][1:4], a[2][0:5]..
# print(res)