import sys
# 시간제한 2초 -> 1초당 5천만까지 허용한다고함. 일반적으론 2천만으로 생각하는게 좋음. 그래서 5000000*22 약 1억의 연산정도 안에서 해결해야 해서 O(nlogn)인 병합정렬 등 고급정렬로 풀어야함. 그런데 sort() 라이브러리가 구현해줬음

if __name__=="__main__":
  input=sys.stdin.readline
  N,K=map(int,input().split())
  a=list(map(int,input().split()))
  a.sort()
  print(a[K-1])
  