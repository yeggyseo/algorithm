seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth

    return nth


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    ways = 1
    currentIndex = 0

    for seat in fixed_seat_array:
        seatIndex = seat - 1
        count = fibo_dynamic_programming(seatIndex - currentIndex, memo)
        ways *= count
        currentIndex = seatIndex + 1
    count = fibo_dynamic_programming(total_count - currentIndex, memo)
    ways *= count
    return ways

print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))