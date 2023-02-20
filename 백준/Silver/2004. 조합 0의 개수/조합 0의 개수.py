import sys
# nCr = n!/(n-r)!r! - 몰랐음
# n!의 0의 개수 - ((n-r)!의 0의 개수 + r!의 0의 개수)
# 팩토리얼의 0의 개수 편하게 구하는 법 - 몰랐음
# 100!은 1부터 100까지 다 곱한거고 거기서 5가 몇개 있느냐를 찾는거니까 5,10,15,20... 25, 50..은 5가 두번..
# 총 24개

# 끝자리가 0이라는 것은 10의 배수를 의미하고, 10은 2,5로 구성되어 있다. 2와 5가 짝이 맞아야 10이 되므로 2의 개수와 5의 개수 중 더 작은게 10의 개수

# n!중에 k가 몇번 곱해져 있는지
def count_number(n,k):
  count=0
  while n:
    n//=k
    count+=n
  return count

if __name__=="__main__":
  input=sys.stdin.readline
  n,m=map(int,input().split())
  
  five_count=count_number(n,5)-(count_number(m,5)+count_number(n-m,5))
  two_count=count_number(n,2)-(count_number(m,2)+count_number(n-m,2))
  answer=min(five_count,two_count)
  print(answer)
  
  