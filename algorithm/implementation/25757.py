game = {"Y": 1, "F": 2, "O": 3}
N, play = input().split()
N = int(N)
people = set()
for i in range(int(N)):
    people.add(input())
print(int(len(people) / game[play]))
