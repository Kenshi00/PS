import sys

if __name__=="__main__":
  input=sys.stdin.readline
  E,S,M=map(int,input().split())
  e=1
  s=1
  m=1
  year=1
  while True:
    if E==e and S==s and M==m:
      print(year)
      break
    else:
      e+=1
      s+=1
      m+=1
      year+=1
      if not 1<=e<=15:
        e=1
      if not 1<=s<=28:
        s=1
      if not 1<=m<=19:
        m=1
      
        