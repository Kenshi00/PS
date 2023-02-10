import sys

# 중복 순열 확장판 
# 1. 순열 (ch[i]==0 같은 체크 배열 추가해서 1,1 2,2 같은거 없앰)
# 2. 조합 (s 인수 추가해서 for문의 시작점을 바꿈 - 상태트리 변경)

def DFS(L,s):
  global cnt
  if L==M:
    cnt+=1
    for i in range(M):
      print(res[i],end=' ')
    print()
  else:
    for i in range(s,N+1): # 1 ~ 4
        res[L]=i
        DFS(L+1,i+1) # 이부분 헷갈

if __name__=="__main__":
  input=sys.stdin.readline
  
  N,M=map(int,input().split())
  res=[0]*M
  cnt=0
  DFS(0,1)
  print(cnt)