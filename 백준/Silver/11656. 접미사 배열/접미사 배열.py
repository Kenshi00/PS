import sys

if __name__=="__main__":
  input=sys.stdin.readline
  S=input().rstrip()
  a=[]
  for i in range(len(S)):
    a.append(S[i:])
  a.sort()
  for x in a:
    print(x)