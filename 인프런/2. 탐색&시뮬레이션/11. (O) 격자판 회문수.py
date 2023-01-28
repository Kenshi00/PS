import sys

input=sys.stdin.readline

a=[list(map(int,input().split())) for _ in range(7)]

cnt=0

#  ㅡ 자모양 구하기
for i in range(7): # 0,0 0,1 0,2  1,0 1,1 1,2 ...
  for j in range(3):
    tmp=a[i][j:j+5]
    if tmp == tmp[::-1]:
      cnt+=1
tmp.clear()

# 2차원 배열 거꾸로 돌려서
b=[[0]*7 for _ in range(7)]
for i in range(7):
  for j in range(7):
    b[i][j]=a[j][i]

# 다시 ㅡ 자모양 구하기 == (ㅣ자모양 구하기)
for i in range(7): # 0,0 0,1 0,2  1,0 1,1 1,2 ...
  for j in range(3):
    tmp=b[i][j:j+5]
    if tmp == tmp[::-1]:
      cnt+=1

print(cnt)