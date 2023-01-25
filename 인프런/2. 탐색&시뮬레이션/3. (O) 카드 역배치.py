import sys

input=sys.stdin.readline

arr=[0]*21
for i in range(1,21):
  arr[i]=i

for i in range(10):
  a,b=map(int,input().split())
  arr[a:b+1]=arr[b:a-1:-1]

# arr.pop(0) 하면 맨 앞 한 개를 없앨 수 있다.
# arr.pop() 하면 맨 뒷 한 개를 없앨 수 있다.
for i in range(1,21):
  print(arr[i], end=' ')
