class DynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.size = 0
        self.resize_factor = resize_factor

    def insert_at_index(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        self.array.insert(index, element)
        self.size += 1
        self._resize_if_needed()

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array.pop(index)
        self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate_right(self, k):
        if self.is_empty() or k <= 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        self.array.reverse()

    def append(self, element):
        self.array.append(element)
        self.size += 1
        self._resize_if_needed()

    def prepend(self, element):
        self.array.insert(0, element)
        self.size += 1
        self._resize_if_needed()

    def merge(self, other):
        self.array.extend(other.array)
        self.size += other.size
        self._resize_if_needed()

    def get_middle(self):
        if self.is_empty():
            return None
        return self.array[self.size // 2]

    def index_of(self, element):
        try:
            return self.array.index(element)
        except ValueError:
            return -1

    def _resize_if_needed(self):
        if len(self.array) > self.size * self.resize_factor:
            self.array = self.array[:self.size]

    def __str__(self):
        return str(self.array)

