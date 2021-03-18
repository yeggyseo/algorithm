# checks if a sublist in a list.
# converts the parent list into a hash set and lookup from a sublist

# O(n) time


shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    for o in orders:
        if o not in set(menus):
            return False
    return True


print(is_available_to_order(shop_menus, shop_orders))
