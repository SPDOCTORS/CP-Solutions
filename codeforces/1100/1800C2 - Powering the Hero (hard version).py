import heapq
t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    heap=[]
    ans=0
    for x in s:
        if x>0:
            heapq.heappush(heap,-x)
        else:
            if heap:
                largest=-heapq.heappop(heap)
                ans+=largest
    print(ans)