class OrderedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []

    def add(self, val: float) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: float) -> bool:
        if val not in self.data_map:
            return False

        last_element = self.data[-1]
        val_position = self.data_map[val]

        self.data_map[last_element] = self.data_map[val]
        self.data[-1], self.data[val_position] = self.data[val_position], self.data[-1]

        self.data.pop()
        self.data_map.pop(val)

        return True

    def __getitem__(self, index):
        return self.data[index]


instance = OrderedSet()
instance.add(5)
print(instance[0])
