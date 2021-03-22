# goes through the list leftward (stack)
# checks if tha height of the tower is less than any of the
# prior towers. If smaller, return the index of the hitting tower.
# For example, [6, 9, 5, 7, 4] will return [0, 0, 2, 2, 4]
# because the last element, 4, is less than 7, which is index 4
# second to last element is less than 9, which has index of 2
# and so on and so on

# O(n^2) time


top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    res = [0] * len(heights)

    while heights:
        h = heights.pop()

        for i in range(len(heights) - 1, 0, -1):
            if heights[i] > h:
                res[len(heights)] = i + 1
                break
    return res


print(get_receiver_top_orders(top_heights))