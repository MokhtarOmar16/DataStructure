class Node:
    def __init__(self,data) -> None:
        self.value = data
        self.back = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    def insertLast(self , data):
        Newdata = Node(data)
        if self.head is None:
            self.head = Newdata
            self.tail = Newdata
        else:
            Newdata.back = self.tail
            self.tail.next = Newdata
            self.tail = Newdata

        self.length += 1

    def insertFirst(self , data):
        Newdata = Node(data)
        if self.head is None:
            self.head = Newdata
            self.tail = Newdata
        else:
            Newdata.next = self.head
            self.head.back = Newdata
            self.head = Newdata
        self.length += 1 
    
    
    def deleteFirst(self):
        self.head = self.head.next
        self.head.back = None
        self.length -= 1

    def deleteLast(self):
        self.tail = self.tail.back
        self.tail.next = None
        self.length -= 1
    
    def delete(self,node :Node ):
        if node == self.head : 
            self.deleteFirst()
            return
        if node == self.tail : 
            self.deleteFirst()
            return
        
        parent = self.findParent(node)
        parent.next = node.next
        self.length -= 1

    def find(self, data) -> Node:
        loop = self.head
        while True:
            if loop.value == data:
                return loop
            if loop.next == None:
                return
            loop = loop.next 


    def printAll(self):
        loop = self.head
        while True:
            print(f"{loop.value} -> " , end= "")
            loop = loop.next
            if loop is None : 
                print()
                break
    
    def insertBefore(self, node:Node, data):
        newNode = Node(data)
        newNode.next = node

        if node == self.head:
            self.head.back = newNode
            self.head = node
            return
        
        newNode.back = node.back
        node.back.next = newNode
        node.back = newNode
        
        self.length += 1 
    
    def insertAfter(self, node: Node, data):
        newNode = Node(data)
        newNode.next = node.next
        newNode.back = node 
        
        node.next = newNode 
        if newNode.next == None :
            self.tail = newNode
        else:
            newNode.next.back = newNode
        self.length += 1 

