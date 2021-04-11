import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    count = currentDateIndex = 0
    maxHeap = []

    while stock < k:
        for dateIndex in range(currentDateIndex, len(dates)):
            if dates[dateIndex] <= stock:
                heapq.heappush(maxHeap, -supplies[dateIndex])
            else:
                currentDateIndex = dateIndex
                break
        count += 1
        stock += -heapq.heappop(maxHeap)
    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))