N, score, P = map(int, input().split())
rank_score = []
my_rank = -1
rank = [1]
if N > 0:
    rank_score = list(map(int, input().split()))
rank_score.append(score)
rank_score.sort()
rank_score.reverse()
for i in range(1, len(rank_score)):
    if rank_score[i] < rank_score[i - 1]:
        rank.append(i + 1)
    else:
        rank.append(rank[-1])
for i in range(len(rank_score)-1, -1, -1):
    if rank_score[i] == score:
        my_rank = i + 1
        break
if my_rank > P:
    print(-1)
else:
    print(rank[my_rank-1])
