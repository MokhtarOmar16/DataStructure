from singlelinkedlist import SingleLinkedList
class Queue:
    def __init__(self) -> None:
        self.__data_list = SingleLinkedList()
    
    def enqueue(self, data):
        self.__data_list.insertLast(data)
    
    def dequeue(self):
        out = self.__data_list.head.value
        self.__data_list.deleteHead()
        return out
    
    def peek(self):
        if self.__data_list.head is None : return
        return self.__data_list.head.value
    
    def is_Empty(self):
        return self.__data_list.length <= 0
    
    def size(self):
        return self.__data_list.length
    
    def printAll(self):
        self.__data_list.printAll()