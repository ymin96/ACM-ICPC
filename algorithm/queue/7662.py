import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    maxHeap = []
    minHeap = []
    maxDelete = []
    minDelete = []
    for i in range(k):
        a, b = map(str, input().split())
        b = int(b)
        if a == "I":
            heapq.heappush(maxHeap, -b)
            heapq.heappush(minHeap, b)
        elif a == "D":
            if b == 1 and len(maxHeap) > 0:
                t = heapq.heappop(maxHeap)
                heapq.heappush(minDelete, -t)
            elif b == -1 and len(minHeap) > 0:
                t = heapq.heappop(minHeap)
                heapq.heappush(maxDelete, -t)
            while minHeap != [] and minDelete != [] and minHeap[0] == minDelete[0]:
                heapq.heappop(minHeap)
                heapq.heappop(minDelete)
            while maxHeap != [] and maxDelete != [] and maxHeap[0] == maxDelete[0]:
                heapq.heappop(maxHeap)
                heapq.heappop(maxDelete)
            if maxHeap == [] or minHeap == []:
                maxHeap = []
                minHeap = []
                maxDelete = []
                minDelete = []

    if maxHeap == [] or minHeap == []:
        print("EMPTY")
        continue
    maxValue = -maxHeap[0]
    minValue = minHeap[0]
    if minValue > maxValue:
        print("EMPTY")
    else:
        print(str(maxValue) + " " + str(minValue))
