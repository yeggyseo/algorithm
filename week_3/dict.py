class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        i = hash(key) % len(self.items)
        self.items[i] = value

    def get(self, key):
        i = hash(key) % len(self.items)
        return self.items[i]


d = Dict()
d.put("test", 3)
print(d.get("test"))
