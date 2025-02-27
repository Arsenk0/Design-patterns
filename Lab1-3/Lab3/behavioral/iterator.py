class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        item = self.collection[self.index]
        self.index += 1
        return item

# Demo
collection = [1, 2, 3, 4]
iterator = Iterator(collection)
while iterator.has_next():
    print(iterator.next())
