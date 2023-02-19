import sys
# 발견할 규칙이 그냥 최대공약수를 구하는 것이었다.
# 내가 한걸로는 시간초과가 났었는데, 유클리드 호제법으로 하면 되는걸 보니 반복적으로 나머지 연산을 함에 따라 빠르게 연산이 되는 것 같다.

# 유클리드 호제법 (최대공약수 구하기) - 외워두자!
# Math.gcd(a,b) 를 사용해도 된다.

def GCD(a,b):
  if b==0:
    return a
  else:
    return GCD(b,a%b)

if __name__=="__main__":
  input=sys.stdin.readline
  a,b=map(int,input().split())
  print('1'*GCD(a,b))
  

  # mod=0
  # res=0

  # if a>b:
  #   mod=divmod(a,b)
  #   mod=mod[1]
  # else:
  #   mod=divmod(b,a)
  #   mod=mod[1]
  # if mod==0:
  #   res=min(a,b)
  # else:
  #   res=mod
  
  # answer=''
  # for _ in range(res):
  #   answer+='1'
  # print(answer)
