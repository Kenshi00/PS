import sys

# lt rt를 0,1로 설정하고 while True로 돌리고 sum 결과가 어떻든 A[lt,rt] 값을 더하고 나서 - lt,rt 를 증가시킨다

input=sys.stdin.readline

N,M=map(int,input().split())

A=list(map(int,input().split()))

cnt=0
lt=0
rt=1
sum=A[0]
while True:
  if sum<M:
    if rt<N:
      sum+=A[rt]
      rt+=1
    else:
      break
  elif sum==M:
    cnt+=1
    sum-=A[lt]
    lt+=1
  else:
    sum-=A[lt]
    lt+=1
print(cnt)

# 시간 초과

# tmp=0 # temporary
# res=0
# while tmp<N: # 0~7
#   for i in range(N-tmp): # i = 0~7
#     j=i+tmp # i=0, j=0  i=1, j=1 ...
#     if sum(A[i:j+1])==M: # A[0:1]
#       res+=1
#     j=0
#   tmp+=1
# print(res)



