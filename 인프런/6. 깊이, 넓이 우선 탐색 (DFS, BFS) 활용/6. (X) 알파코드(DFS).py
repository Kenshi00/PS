import sys

def DFS(L,P):
  global cnt
  if L==N:
    cnt+=1
    for i in range(P): # 0 ~ 4
      print(chr(res[i]+64),end='')
    print()
  else:
    for i in range(1,27): # 1~26
      if i==code[L]:
        res[P]=i
        DFS(L+1,P+1)
      elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
        res[P]=i
        DFS(L+2,P+1)

if __name__=="__main__":
  input=sys.stdin.readline
  code=list(map(int,input().rstrip()))
  N=len(code)
  code.insert(N,-1)
  res=[0]*(N+3)
  cnt=0
  DFS(0,0)
  print(cnt)

# 결과가 나오긴 하지만 time limit에 막힌다
# def DFS(L):
#   global answer
#   if sum(res)>len(N):
#     return
#   if sum(res)==len(N):
#     k=0
#     cnt=0
#     ch=''
#     for i in res:
#       tmp=N[k:k+i]
#       if len(tmp)==2 and N[k]=='0':
#         break
#       tmp=int(tmp)
#       if 0<tmp<=26:
#         cnt+=1
#         ch+=chr(tmp+64)
#       else:
#         break
#       k+=i
#     if cnt==len(res):
#       print(ch)
#       answer+=1
#   if L>len(N):
#     return
#   else:
#     for i in range(1,3): # 1,2
#       res.append(i)
#       DFS(L+1)
#       res.pop()

# if __name__=="__main__":
#   input=sys.stdin.readline
#   N=input().rstrip()
#   res=[]
#   answer=0
#   DFS(0)
#   print(answer)