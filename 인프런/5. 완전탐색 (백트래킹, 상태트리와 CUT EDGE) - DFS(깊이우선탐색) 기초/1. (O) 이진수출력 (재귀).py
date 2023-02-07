import sys

input=sys.stdin.readline

# DFS 재귀는 스택 원리, 거의 무조건 if else
# return은 함수 종료
def DFS(x):
  if x==0:
    return
  else:
    DFS(x//2)
    print(x%2,end='')

if __name__=="__main__":
  N=int(input())
  DFS(N)
