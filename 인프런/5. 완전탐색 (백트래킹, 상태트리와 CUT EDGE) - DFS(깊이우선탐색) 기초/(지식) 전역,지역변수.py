# 전역변수와 지역변수

def DFS1():
  cnt=3
  print(cnt) # 지역변수 출력

def DFS2():
  global cnt # cnt는 전역변수를 의미하는 것이다! 선언
  if cnt==5:
    print(cnt) 

if __name__=="__main__":
  cnt=5 # 전역변수
  DFS1()
  DFS2()
  print(cnt)

# 그럼 왜 리스트는 global 없이 써도 전역변수로 알아서 적용이 되는가?
# 전역변수처럼 새로 만드는 것이 아니고 참조하는 것이기 때문