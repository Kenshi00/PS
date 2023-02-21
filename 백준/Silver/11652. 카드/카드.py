import sys
# dict를 이용한다
# dict[i]=val -> {i:val}
# dict.get(key,0)+1
# for key,value in dict.items()

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  a=[]
  dict={}
  for _ in range(N):
    tmp=int(input())
    # key값이 있으면 그 value return 없으면 0
    dict[tmp]=dict.get(tmp,0)+1
  
  k=0
  v=0
  for key,value in dict.items():
    if value>v:
      v=value
      k=key
    elif value==v:
      k=min(k,key)
  print(k)
