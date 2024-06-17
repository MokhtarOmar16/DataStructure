from singlelinkedlist import SingleLinkedList

class Stack:
    def __init__(self) -> None:
        self.__data_list = SingleLinkedList()
    
    def push(self, data):
        self.__data_list.insertFirst(data)
    
    def pop(self):
        head = self.__data_list.head.value
        self.__data_list.deleteHead()
        return head
    
    def peek(self):
        return self.__data_list.head.value
    
    def is_Empty(self):
        return self.__data_list.length <= 0
    
    def printAll(self):
        self.__data_list.printAll()