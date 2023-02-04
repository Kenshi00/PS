import sys

input=sys.stdin.readline

N=int(input())
dict={} # p=dict()
for _ in range(N):
  tmp=input().strip()
  dict[tmp]=0
for _ in range(N-1):
  tmp=input().strip()
  dict[tmp]+=1
# dictionary의 items() 이터레이터 함수
for key, value in dict.items():
  if value==0:
    print(key)
  