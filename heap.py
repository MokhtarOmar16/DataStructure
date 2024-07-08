class Heap:

    def __init__(self):
        self._data_list = []
        self._size = 0

    def insert(self, data):
        i = self._size
        self._data_list.append(data)
        self._size += 1

        parent_index = (i - 1) // 2
        while i != 0 and self._data_list[i] < self._data_list[parent_index]:
            self._data_list[i], self._data_list[parent_index] = self._data_list[parent_index], self._data_list[i]
            i = parent_index
            parent_index = (i - 1) // 2

    def pop(self):
        if self._size == 0:
            return None
        i = 0
        data = self._data_list[i]

        self._data_list[i] = self._data_list[self._size - 1]
        self._data_list.pop()
        self._size -= 1

        left_index = 2 * i + 1
        while left_index < self._size:
            right_index = 2 * i + 2
            smaller_index = left_index
            if right_index < self._size and self._data_list[right_index] < self._data_list[left_index]:
                smaller_index = right_index

            if self._data_list[smaller_index] >= self._data_list[i]:
                break

            self._data_list[i], self._data_list[smaller_index] = self._data_list[smaller_index], self._data_list[i]
            i = smaller_index
            left_index = 2 * i + 1

        return data

    def print_heap(self):
        print(self._data_list)

    def size(self):
        return self._size