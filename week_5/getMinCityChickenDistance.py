import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    chickenLocationList = []
    homeLocationList = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                homeLocationList.append([i, j])
            elif city_map[i][j] == 2:
                chickenLocationList.append([i, j])
    chickenLocationMCombinations = list(itertools.combinations(chickenLocationList, m))
    minDistance = sys.maxsize

    for combination in chickenLocationMCombinations:
        distance = 0
        for homeR, homeC in homeLocationList:
            minChickenDistance = sys.maxsize
            for chickenLocation in combination:
                minChickenDistance = min(
                    minChickenDistance,
                    abs(homeR - chickenLocation[0]) + abs(homeC - chickenLocation[1])
                )
            distance += minChickenDistance

        minDistance = min(minDistance, distance)

    return minDistance

# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!