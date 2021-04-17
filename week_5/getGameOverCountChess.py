k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def getDWhenGoBack(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(chess_map)
    currentStackedHorseMap = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        currentStackedHorseMap[r][c].append(i)
    turnCount = 1

    while turnCount <= 1000:
        for horseIndex in range(horse_count):
            r, c, d = horse_location_and_directions[horseIndex]
            newR = r + dr[d]
            newC = c + dc[d]

            if not 0 <= newR < n or not 0 <= newC < n or game_map[newR][newC] == 2:
                newD = getDWhenGoBack(d)
                horse_location_and_directions[horseIndex][d] = newD
                newR = r + dr[newD]
                newC = c + dc[newD]

            if not 0 <= newR < n or not 0 <= newC < n or game_map[newR][newC] == 2:
                continue

            movingHorseIndexArray = []
            for i in range(len(currentStackedHorseMap[r][c])):
                currentHorseIndex = currentStackedHorseMap[r][c][i]
                if horseIndex == currentHorseIndex:
                    movingHorseIndexArray = currentStackedHorseMap[r][c][i:]
                    currentStackedHorseMap[r][c] = currentStackedHorseMap[r][c][:i]
                    break
            if game_map[newR][newC] == 1:
                movingHorseIndexArray = reversed(movingHorseIndexArray)

            for movingHorseIndex in movingHorseIndexArray:
                currentStackedHorseMap[newR][newC].append(movingHorseIndex)
                horse_location_and_directions[movingHorseIndex][0], horse_location_and_directions[movingHorseIndex][1] = newR, newC

            if len(currentStackedHorseMap[newR][newC]) >= 4:
                return turnCount

        turnCount += 1
    return -1

print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
