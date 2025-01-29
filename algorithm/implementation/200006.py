class Player:
    def __init__(self, level, name):
        self.name = name
        self.level = level


class Room:
    def __init__(self, player, maxSize):
        self.playerList = []
        self.playerList.append(player)
        self.minLevel = player.level - 10
        self.maxLevel = player.level + 10
        self.maxSize = maxSize

    def add_player(self, player):
        self.playerList.append(player)

    def get_size(self):
        return len(self.playerList)

    def print(self):
        self.playerList.sort(key=lambda x: x.name)
        if len(self.playerList) < self.maxSize:
            print("Waiting!")
        else:
            print("Started!")
        for player in self.playerList:
            print(str(player.level) + " " + player.name)


p, m = map(int, input().split())
playerList = []
for i in range(p):
    level, name = map(str, input().split())
    level = int(level)
    playerList.append(Player(level, name))
roomList = []
for player in playerList:
    check = True
    for room in roomList:
        if room.get_size() < m and room.minLevel <= player.level <= room.maxLevel:
            check = False
            room.add_player(player)
            break
    if check:
        roomList.append(Room(player, m))
for room in roomList:
    room.print()
