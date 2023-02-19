import sys

if __name__=="__main__":
  input=sys.stdin.readline
  N,B=map(int,input().split())
  answer=''
  while N!=0:
    if 0<=N%B<10:
      answer+=str(N%B)
    else: # 10~35
      answer+=chr(N%B+55)
    N=N//B
  print(answer[::-1])
  