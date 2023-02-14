import sys

if __name__=="__main__":
  input=sys.stdin.readline
  A,B,C,D=map(str,input().split())
  print(int(A+B)+int(C+D))