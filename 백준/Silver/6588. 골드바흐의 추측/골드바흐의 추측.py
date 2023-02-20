import sys,math

if __name__=="__main__":
  input=sys.stdin.readline
  # 아리스토텔레스 소수 체
  # 백만이 들어오면 이렇게 시간초과가 나기 때문에 range에서 범위를 루트로 줄여야 한다.
  # 루트만큼만 확인해도 전체를 확인할 수 있다. - 외우기
  r=1000000
  ch=[0]*(r+1)
  for i in range(2,1001):
    if ch[i]==0:
      for j in range(2*i,r+1,i):
        if ch[j]==0:
          ch[j]=1

  while True:
    n=int(input())
    cnt=0
    if n==0:
      break
    for i in range(3,n,2):
      if ch[i]==0 and ch[n-i]==0:
        print(n,'=',i,'+',n-i)
        cnt=1
        break
    if cnt==0:
      print("GoldBach's conjecture is wrong.")