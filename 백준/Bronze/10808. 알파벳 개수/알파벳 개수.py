import sys

if __name__=="__main__":
  input=sys.stdin.readline
  S=input().rstrip()
  a=[0]*200
  for x in S:
    a[ord(x)]+=1
  for x in a[97:123]:
    print(x, end=' ')