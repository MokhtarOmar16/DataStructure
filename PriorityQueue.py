class Item:

    def __init__(self, priority: int, data: int):
        self.priority = priority
        self.data = data


class PriorityQueue:
    def __init__(self):
        self._data_list = []
        self._size = 0

    def enqueue(self, priority, data):
        i = self._size
        self._data_list.append(Item(priority, data))
        self._size += 1
        parent_index = (i - 1) // 2
        # Heap-up operation to maintain the heap property.
        while i != 0 and self._data_list[i].priority < self._data_list[parent_index].priority:
            temp = self._data_list[i]
            self._data_list[i] = self._data_list[parent_index]
            self._data_list[parent_index] = temp
            i = parent_index
            parent_index = (i - 1) // 2

    def dequeue(self):
        if self._size == 0: return None
        i = 0
        data = self._data_list[i].data
        priority = self._data_list[i].priority
        self._data_list[i] = self._data_list[self._size - 1]
        self._data_list[self._size - 1] = None
        self._size -= 1
        left_index = 2 * i + 1
        while left_index < self._size:
            right_index = 2 * i + 2
            smaller_index = left_index
            if right_index < self._size and self._data_list[right_index].priority < self._data_list[left_index].priority:
                smaller_index = right_index
            if self._data_list[smaller_index].priority >= self._data_list[i].priority:
                break
            temp = self._data_list[i]
            self._data_list[i] = self._data_list[smaller_index]
            self._data_list[smaller_index] = temp
            i = smaller_index
            left_index = 2 * i + 1
        return Item(priority, data)

    def hasData(self):
        return self._size > 0

    def print(self):
        print(self._data_list)

    def size(self):
        return self._size

