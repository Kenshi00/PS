import sys
# DFS 안에 전위(부왼오), 중위(왼부오), 후위(왼오부) 순회

def DFS(v):
  if v>7:
    return
  else:
    # print(v,end=' ')가 결국은 함수 본연의 일 - 나중엔 복잡하게 바뀜.
    # 전위 - 대부분
    # print(v,end=' ')
    DFS(v*2) # left
    # 중위 - 거의x
    # print(v,end=' ')
    DFS(v*2+1) # right
    # 후위 - 병합정렬
    # print(v,end=' ')

if __name__=="__main__":
  DFS(1)