import sys

# for idx, x in enumerate(score): 과 같은 방식으로
# index와 value 값에 접근할 수 있다는 것을 기억하자.

input=sys.stdin.readline

N=int(input())
score=list(map(int, input().split()))

ave=round(sum(score)/len(score))
tmp=float('inf')
num=0

for idx, x in enumerate(score): # idx=인덱스 x=값
  val=abs(ave-x)
  if val<tmp:
    tmp=val
    num=idx+1
  elif val==tmp:
    if score[idx]>score[num]:
      num=idx
print(ave,num+1)


# 내 풀이
# for i in range(len(score)):
#   val=abs(ave-score[i])
#   if val<tmp:
#     tmp=val
#     num=i
#   elif val==tmp:
#     if score[i]>score[num]:
#       num=i
#     elif i<num:
#       num=i

# print(ave,num+1)