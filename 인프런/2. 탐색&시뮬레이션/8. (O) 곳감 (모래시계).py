import sys


input=sys.stdin.readline

N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]

M=int(input())
for _ in range(M): # 0 1 2
  r,d,c=map(int,input().split())

  # 훨씬 편한 풀이 (insert, pop() - 맨 뒤에 것 꺼냄, pop(0) - 맨 앞에 것 꺼냄)

  # 2 0 3 이라 치면,
  if d==0:
    for _ in range(c): # c=3번 동안 반복
      a[r-1].append(a[r-1].pop(0)) # 리스트의 앞의 수를 빼고 다시 넣음(뒤로 감)
  else:
    for _ in range(c):
      a[r-1].insert(0,a[r-1].pop())
      
res=0
s=0
e=N-1
for i in range(N):
  res+=sum(a[i][s:e+1])

  if i < N//2:
    s+=1
    e-=1
  else:
    s-=1
    e+=1

print(res)

  # 나의 복잡한 풀이

  # tmp=[]
  # if d==0:
  #   for i in range(N):
  #     tmp.append(a[r-1][(i+c)%N])
  # else:
  #   for i in range(N):
  #     tmp.append(a[r-1][(i+(N-c))%N])
  # a[r-1],tmp=tmp,a[r-1]
  # tmp.clear()

# for i in range(N):
#   print(a[i])

# res=0
# s=0
# e=N
# for i in range(N):
#   res+=sum(a[i][s:e])

#   if i < N//2:
#     s+=1
#     e-=1
#   else:
#     s-=1
#     e+=1

# print(res)


