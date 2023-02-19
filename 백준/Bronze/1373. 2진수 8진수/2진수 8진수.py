import sys

# 내장함수로 하지 않으면 시간초과가 뜬다. 그냥 외워야 할듯하다.

if __name__=="__main__":
  input=sys.stdin.readline
  # int() 함수의 두번째 인자는 진법을 의미
  N=int(input(),2)
  # oct() - 8진수로 출력 (앞에 8진수표기 지움)
  print(oct(N)[2:])

# if __name__=="__main__":
#   input=sys.stdin.readline
#   N=input().rstrip()
#   if len(N)%3==2:
#     N='0'+N
#   elif len(N)%3==1:
#     N='00'+N
  
#   res=''
#   while True:
#     res+=str(int(N[0])*4+int(N[1])*2+int(N[2])*1)
#     N=N[3:]
#     if len(N)==0:
#       break
#   print(res)

