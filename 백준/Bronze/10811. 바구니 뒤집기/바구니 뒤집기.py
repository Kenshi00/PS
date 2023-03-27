N,M=map(int,input().split())
arr=[x for x in range(N+1)] # 0 1 2 3 4 5
for _ in range(M):
    x,y=map(int,input().split())
    tmp=arr[x:y+1]
    arr[x:y+1]=tmp[::-1]
for i in range(1,N+1):
    print(arr[i], end=' ')