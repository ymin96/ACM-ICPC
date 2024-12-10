index = ['a', 'e', 'i', 'o', 'u']


def password(word):
    check = False

    for i in index:
        if i in word:
            check = True
    if not check:
        return False

    for i in range(1, len(word) - 1):
        cnt = 0
        for j in range(-1, 2):
            if word[i + j] in index:
                cnt += 1
        if cnt == 3 or cnt == 0:
            return False

    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1] and word[i] != 'e' and word[i] != 'o':
            return False

    return True


while True:
    word = input()
    if word == "end":
        break
    success = password(word)
    if success:
        print('<' + word + '> is acceptable.')
    else:
        print('<' + word + '> is not acceptable.')
