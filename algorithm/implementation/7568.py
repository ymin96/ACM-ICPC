N = int(input())
answer = []
input_data = []
for _ in range(N):
    input_data.append(list(map(int, input().split())))

for i in range(N):
    cnt = 1
    for j in range(N):
        if input_data[i][0] < input_data[j][0] and input_data[i][1] < input_data[j][1]:
            cnt += 1
    answer.append(cnt)

for i in answer:
    print(i, end=" ")
