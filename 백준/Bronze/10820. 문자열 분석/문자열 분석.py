import sys

if __name__=="__main__":
  while True:
    try:
      tmp=input()
      a=[0]*4 # 소문자, 대문자, 숫자, 공백
      for x in tmp:
        if 'a'<=x<='z':
          a[0]+=1
        elif 'A'<=x<='Z':
          a[1]+=1
        elif '0'<=x<='9':
          a[2]+=1
        else:
          a[3]+=1
      for i in a:
        print(i,end=' ')
      print()
    except EOFError:
      break