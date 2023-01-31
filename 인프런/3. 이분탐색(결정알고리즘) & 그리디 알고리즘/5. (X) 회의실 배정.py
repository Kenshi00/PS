import sys

# 그리디 문제는 어떤 상황마다 가장 좋은 결과를 선택하면 되는 것. 대부분의 그리디는 정렬과 동반되서 문제 풀이

# 틀린 이유
# 끝나는 시점을 기준으로 정렬해야 하는 아이디어 몰랐음.
# 튜플 정렬하기 (두 번째 원소로 정렬하기) 기능 몰랐음.

input=sys.stdin.readline

n=int(input())

arr=[]
for i in range(n):
  a,b=map(int,input().split())
  arr.append((a,b))

arr.sort(key=lambda x:x[1])

tmp=0
cnt=0
for x in arr:
  if tmp<=x[0]:
    cnt+=1
    tmp=x[1]
    
print(cnt)  
  
  

# print(res)
