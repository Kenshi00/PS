import sys

input=sys.stdin.readline

first=list(input().strip())
second=list(input().strip())

dict1={}
dict2={}
for i in first:
  # dict1에 i라는 key 값이 있으면 그 value return, 없으면 0 리턴 - dict의 get() 함수 기억할것!
  # dict1[i]=j -> dict1에다가 { 'i' : 'j' , ...} (key:value)
  dict1[i]=dict1.get(i,0)+1
for i in second:
  dict2[i]=dict2.get(i,0)+1

if dict1==dict2:
  print("YES")
else :
  print("NO")
# cnt=0
# dict.items() - 매우 유용한 함수 인듯
# for key,value in dict.items():
#   if value==0:
#     cnt+=1
# if cnt==len(dict):
#   print('YES')
# else:
#   print('NO')