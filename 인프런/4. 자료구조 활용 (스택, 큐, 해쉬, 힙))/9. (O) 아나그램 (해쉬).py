import sys

input=sys.stdin.readline

first=list(input().strip())
second=list(input().strip())

dict={}

for i in first:
  if i not in dict:
    dict[i]=1
  else:
    dict[i]+=1

for i in second:
  if i not in dict:
    dict[i]=1
  else:
    dict[i]-=1
cnt=0
for key,value in dict.items():
  if value==0:
    cnt+=1
if cnt==len(dict):
  print('YES')
else:
  print('NO')