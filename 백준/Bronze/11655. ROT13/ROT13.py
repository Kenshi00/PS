import sys

if __name__=="__main__":
  input=sys.stdin.readline
  S=input().rstrip()
  for x in S:
    if 'a' <= x <= 'm' or 'A' <= x <= 'M':
      print(chr(ord(x)+13),end='')
    elif 'n' <= x <= 'z' or 'N' <= x <= 'Z':
      print(chr(ord(x)-13),end='')
    else:
      print(x,end='')
