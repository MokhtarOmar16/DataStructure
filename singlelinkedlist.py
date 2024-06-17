class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self) -> None:
        self.lenght = 0
        self.head = None
        self.tail = None
    def insertLast(self , data):
        Newdata = Node(data)
        if self.head is None:
            self.head = Newdata
            self.tail = Newdata
        else:
            self.tail.next = Newdata
            self.tail = Newdata
        self.lenght += 1

    def insertFirst(self , data):
        Newdata = Node(data)
        if self.head is None:
            self.head = Newdata
            self.tail = Newdata
        else:
            Newdata.next = self.head
            self.head = Newdata
        self.lenght += 1 
    
    @property
    def length(self):
        return self.length
    
    def deleteFirst(self):
        self.head = self.head.next
        self.length -= 1

    def deleteLast(self):
        self.tail = self.findParent(self.tail.value)
        self.tail.next = None
        self.length -= 1
    
    def deleteNode(self,node :Node):
        if not isinstance(node,Node):
            return
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
    
    def findParent(self, data) -> Node:

        loop = self.head
        while True:
            if loop.next == None:
                return
            if loop.next.value == data:
                return loop
            loop = loop.next 

    def printAll(self):
        loop = self.head
        while True:
            print(f"{loop.value} -> " , end= "")
            loop = loop.next
            if loop is None : 
                print()
                break
    
    def insertBefore(self, node, data):
        newNode = Node(data)
        parent = self.findParent(node.value)
        parent.next= newNode
        newNode.next = node
        self.lenght += 1 
    
    def insertAfter(self, node, data):
        nextNode = node.next
        newNode = Node(data)
        newNode.next = nextNode
        node.next = newNode
        self.lenght += 1 



