from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def moveUntilWallOrHole(r, c, diffR, diffC, gameMap):
    moveCount = 0
    while gameMap[r + diffR][c + diffC] != "#" and gameMap[r][c] != "0":
        r += diffR
        c += diffC
        moveCount += 1
    return r, c, moveCount


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    redR, redC, blueR, blueC = -1, -1, -1, -1
    queue = deque()
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                redR, redC = i, j
            elif game_map[i][j] == "B":
                blueR, blueC = i, j
    queue.append((redR, redC, blueR, blueC, 1))
    visited[redR][redC][blueR][blueC] = True

    while queue:
        redR, redC, blueR, blueC, count = queue.popleft()

        if count > 10:
            break

        for i in range(4):
            nextRedR, nextRedC, rCount = moveUntilWallOrHole(redR, redC, dr[i], dc[i], game_map)
            nextBlueR, nextBlueC, bCount = moveUntilWallOrHole(blueR, blueC, dr[i], dc[i], game_map)

            if game_map[nextBlueR][nextBlueC] == "O":
                continue
            if game_map[nextRedR][nextRedC] == "O":
                return True
            if nextRedR == nextBlueR and nextRedC == nextBlueC:
                if rCount > bCount:
                    nextRedR -= dr[i]
                    nextRedC -= dc[i]
                else:
                    nextBlueR -= dr[i]
                    nextBlueC -= dc[i]

            if not visited[nextRedR][nextRedC][nextBlueR][nextBlueC]:
                visited[nextRedR][nextRedC][nextBlueR][nextBlueC] = True
                queue.append((nextRedR, nextRedC, nextBlueR, nextBlueC, count + 1))
    return False


print(is_available_to_take_out_only_red_marble(game_map))
