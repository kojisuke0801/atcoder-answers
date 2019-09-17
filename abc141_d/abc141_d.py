from heapq import heappush, heappop

n, m = map(int, input().split())
a_list = list(map(int, input().split()))

hqueue = []
for a in a_list:
    heappush(hqueue, -a)

for i in range(m):
    max_item = -(-heappop(hqueue) // 2)
    heappush(hqueue, max_item)

cost = 0
for i in range(n):
    cost += -heappop(hqueue)

print(cost)
