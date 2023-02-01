import sys

input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))

res=[]
last=0
s=""
# 하나라도 크면 일단 통과시킴
while arr[0]>last or arr[-1]>last:
  # 양 옆 둘 다 큰 경우
  if arr[0]>last and arr[-1]>last:
    if arr[0]<arr[-1]:
      res.append(arr[0])
      arr.pop(0)
      s+="L"
    else:
      res.append(arr[-1])
      arr.pop()
      s+="R"

  # 왼쪽만 큰 경우
  elif arr[0]>last:
    res.append(arr[0])
    arr.pop(0)
    s+="L"

  # 오른쪽만 큰 경우
  else:
    res.append(arr[-1])
    arr.pop()
    s+="R"
  last=res[-1]

print(len(res))
print(s)