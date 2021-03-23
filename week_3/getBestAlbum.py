# Returns most played albums in pairs.
# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
# The given inputs above should return [4, 1, 3, 0]

# O(n^2) time

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    d = {}
    ad = {}
    for i in range(len(genre_array)):
        g = genre_array[i]
        p = play_array[i]

        if g not in d:
            d[g] = p
            ad[g] = [[i, p]]
        else:
            d[g] += p
            ad[g].append([i, p])

    sa = sorted(d.items(), key=lambda item: item[1], reverse=True)

    res = []

    for g, v in sa:
        indexPlayArray = ad[g]
        sortedipa = sorted(indexPlayArray, key=lambda item: item[1], reverse=True)

        for i in range(len(sortedipa)):
            if i > 1:
                break
            res.append(sortedipa[i][0])

    return res


print(get_melon_best_album(genres, plays))