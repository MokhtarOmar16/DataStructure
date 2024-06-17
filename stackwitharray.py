"""
if you coded it in java ,cpp ,c ,c# ..etc
you should add resize() method and edit the remain methods
"""
class Stack:
    def __init__(self) -> None:
        self.__data_list = []
        self.__top_index = -1

    def push(self, data):
        self.__data_list.append(data)
        self.__top_index += 1
    
    def pop(self): 
        if self.__top_index == -1 : return
        data = self.__data_list.pop(self.__top_index) 
        self.__top_index -= 1
        return data
    
    def peek(self):
        return self.__data_list[self.__top_index]

    def printAll(self):
        print(self.__data_list[::-1])
    
    def is_Empty(self):
        return len(self.__data_list) <= 0
    
    def size(self):
        return len(self.__data_list.lenght)