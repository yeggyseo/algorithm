current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def calculateRotationToLeft(d):
    return (d + 3) % 4


def calculateBackIndex(d):
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n, m = len(room_map), len(room_map[0])

    count = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)
        tempd = d

        for i in range(4):
            tempd = calculateRotationToLeft(tempd)
            newr, newc = r + dr[tempd], c + dc[tempd]

            if 0 <= newr < n and 0 <= newc < m and room_map[newr][newc] == 0:
                count += 1
                room_map[newr][newc] = 2
                queue.append([newr, newc, tempd])
                break
            elif i == 3:
                newr, newc = r + dr[(calculateBackIndex(tempd))], c + dc[calculateBackIndex(tempd)]
                queue.append([newr, newc, tempd])

                if room_map[newr][newc] == 1:
                    return count


print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))