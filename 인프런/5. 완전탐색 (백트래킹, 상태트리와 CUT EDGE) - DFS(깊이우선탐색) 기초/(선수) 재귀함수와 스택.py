# 재귀함수와 스택
import sys

input=sys.stdin.readline

def DFS(x):
  if x>0:
    print(x)
    DFS(x-1)

# 파일이 실행되면 여기서부터 시작함
if __name__=="__main__":
  n=int(input())
  DFS(n)