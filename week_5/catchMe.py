from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    while cony_loc < 200000:
        cony_loc += time

        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            curPosition, curTime = queue.popleft()

            newTime = curTime + 1

            newPosition = curPosition - 1
            if newPosition >= 0 and newTime not in visited[newPosition]:
                visited[newPosition][newTime] = True
                queue.append((newPosition, newTime))

            newPosition = curPosition + 1
            if newPosition < 200001 and newTime not in visited[newPosition]:
                visited[newPosition][newTime] = True
                queue.append((newPosition, newTime))

            newPosition = curPosition * 2
            if newPosition < 200001 and newTime not in visited[newPosition]:
                visited[newPosition][newTime] = True
                queue.append((newPosition, newTime))
        time += 1


print(catch_me(c, b))