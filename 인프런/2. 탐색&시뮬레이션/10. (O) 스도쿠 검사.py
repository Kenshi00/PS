import sys

# 강사는 ch[]=1을 이용해서 했음. 체크배열 이용.
input=sys.stdin.readline

a=[list(map(int,input().split())) for _ in range(9)]

def check(a):
  # 1. 스도쿠의 row, column 확인
  for i in range(9):
    ch1=[0]*10
    ch2=[0]*10
    for j in range(9):
      ch1[a[i][j]]=1
      ch2[a[j][i]]=1
    if sum(ch1)!=9 or sum(ch2)!=9:
      return False
  # 2. 4중 for문을 이용한 구역별 확인
  for i in range(3):
    for j in range(3):
      ch3=[0]*10
      for k in range(3):
        for s in range(3):
          ch3[a[i*3+k][j*3+s]]=1
      if sum(ch3)!=9:
        return False
  return True

if check(a)==True:
  print("YES")
else:
  print("NO")
      

# 내 풀이도 맞음!
# def isSdq(a):

#   res1=[]
#   res2=[]
#   res3=[]
#   res4=[]
#   res5=[]
#   for i in range(9): # 0~8
#     for j in range(9): # 0~8
#       res1.append(a[i][j])
#       res2.append(a[j][i])
#     for k in range(1,10):
#       if k not in res1 or k not in res2:
#         return "NO"

#     res3+=res1[0:3]
#     res4+=res1[3:6]
#     res5+=res1[6:9]

#     if i in [2,5,8]:
#       for k in range(1,10):
#         if k not in res3 or k not in res4 or k not in res5:
#           return "NO"
#       res3.clear()
#       res4.clear()
#       res5.clear()

#     res1.clear()
#     res2.clear()
  
#   return "YES"

# print(isSdq(a))