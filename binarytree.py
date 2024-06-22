from collections import deque

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        newNode = TreeNode(data)
        if self.root is None : 
            self.root = newNode
            return
        q :TreeNode= deque()
        q.append(self.root)
        while q :
            cur_node = q.popleft()
            if not cur_node.left :
                cur_node.left = newNode
                return
            else: q.append(cur_node.left)
            
            if not cur_node.right:
                cur_node.right = newNode
                return
            else: q.append(cur_node.right)

    def height(self):
        return self.__height(self.root)
    
    def __height(self,node :TreeNode):
        if node is None :
            return 0 
        return 1 + max(self.__height(node.left), self.__height(node.right))
    


    
    def PreOrder(self):
        self.internalPreOrder(self.root)
        print()

    def internalPreOrder(self, node):
        if node is None:
            return
        print(node.data, "->", end=" ")
        self.internalPreOrder(node.left)
        self.internalPreOrder(node.right)
    
    def find(self, data):
        return self.__find(self.root, data)
        

    def __find(self, node: TreeNode ,data):
        if node is None:
            return None
        if node.data == data:
            return node
        left = self.__find(node.left, data)
        if left is not None:
            return left
        return self.__find(node.right, data)
