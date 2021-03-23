# find a way to get max discount

# O(nlog(n)) time


shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    pi = ci = maxPrice = 0

    while pi < len(prices) and ci < len(coupons):
        maxPrice += prices[pi] * (100 - coupons[ci]) / 100
        pi += 1
        ci += 1

    while pi < len(prices):
        maxPrice += prices[pi]
        pi += 1

    return maxPrice


print(get_max_discounted_price(shop_prices, user_coupons))
