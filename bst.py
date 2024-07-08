class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

class NodeAndParent:

  def __init__(self, node=None, parent=None, isLeft=None):
    self.node = node
    self.parent = parent
    self.isLeft = isLeft


class BinarySearchTree:
    def __init__(self, data= None) -> None:
        if data :
            self.root = TreeNode(data)
        self.root = None

    def isExist(self, data):
        return self.bsFind(data) is not None

    def findNodeAndParent(self, data):
        currentNode = self.root
        parent = None
        nodeAndParentInfo = None
        isLeft = False
        while currentNode is not None:
            if currentNode.data == data:
                nodeAndParentInfo = NodeAndParent(currentNode, parent, isLeft)
                break
            elif currentNode.data > data:
                parent = currentNode
                isLeft = True
                currentNode = currentNode.left
            else:
                parent = currentNode
                isLeft = False
                currentNode = currentNode.right
        return nodeAndParentInfo

    def BSInsert(self, data):
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
            return
        curNode = self.root
        while curNode:
            if data < curNode.data:
                if curNode.left == None:
                    curNode.left = newNode
                    return
                else :
                    curNode = curNode.left
            elif data > curNode.data:
                if curNode.right == None:
                    curNode.right = newNode
                    return
                else :
                    curNode = curNode.right
            else: 
                return "this data is already exist"
                
    def find_data(self, data):
        if not self.root:
            return -1
        curNode = self.root
        while curNode:
            if data < curNode.data:
                if curNode.left == None:
                    return -1
                else :
                    curNode = curNode.left
            elif data > curNode.data:
                if curNode.right == None:
                    return -1
                else :
                    curNode = curNode.right
            else: 
                return curNode

        
    def BsDelete(self, data):
        nodeAndParentInfo = self.findNodeAndParent(data)
        if nodeAndParentInfo.node is None:
            return
        # Node has two children
        if nodeAndParentInfo.node.left is not None and nodeAndParentInfo.node.right is not None:
            self.bsDeleteHasChilds(nodeAndParentInfo.node)
        # Node has one child
        elif nodeAndParentInfo.node.left is not None or nodeAndParentInfo.node.right is not None:
            self.bsDeleteHasOneChild(nodeAndParentInfo.node)
        # Node is a leaf
        else:
            self.bsDeleteLeaf(nodeAndParentInfo)

    def bsDeleteLeaf(self, nodeAndParentInfo):    
        if nodeAndParentInfo.parent is None:
            self.root = None
        else:
            if nodeAndParentInfo.isLeft:
                nodeAndParentInfo.parent.left = None
            else:
                nodeAndParentInfo.parent.right = None

    def bsDeleteHasOneChild(self ,nodeToDelete):
    # Find the node to replace the deleted node with
        
        nodeToReplace = None
        if nodeToDelete.left != None:
            nodeToReplace = nodeToDelete.left
        else:
            nodeToReplace = nodeToDelete.right

        # Replace the deleted node with the replacement node
        nodeToDelete.data = nodeToReplace.data
        nodeToDelete.left = nodeToReplace.left
        nodeToDelete.right = nodeToReplace.right

    def bsDeleteHasChilds(self , nodeToDelete):
        # Find the node to replace the deleted node with
        currentNode = nodeToDelete.right
        parent = None
        while currentNode.left != None:
            parent = currentNode
            currentNode = currentNode.left
        # Replace the deleted node with the replacement node
        if parent != None:
            parent.left = currentNode.right
        else:
            nodeToDelete.right = currentNode.right
        nodeToDelete.data = currentNode.data
        
    def balance(self):
        nodes = []
        self.inOrderToArray(self.root , nodes)
        self.root = self.recursive_balance(len(nodes)-1 , nodes)
    

    def recursive_balance(self, end:int , nodes:list, start = 0,):
        if start > end :return
        mid = (start + end) // 2 
        node = TreeNode(nodes[mid])
        node.left = self.recursive_balance(mid-1, nodes)
        node.right = self.recursive_balance(start=mid+1 ,end=end, nodes=nodes)

        return node
    
    def inOrderToArray(self, node: TreeNode ,nodes: list):
        if node == None: return

        self.inOrderToArray(node.left, nodes)
        nodes.append(node.data)
        self.inOrderToArray(node.right, nodes)

    def InOrder(self):
        self.internalInOrder(self.root)
        print("")

    def internalInOrder(self, node):
        if node is None:
            return
        self.internalInOrder(node.left)
        print(node.data, " -> ", end='')
        self.internalInOrder(node.right)

bTree = BinarySearchTree()


bTree.BSInsert(4)
bTree.BSInsert(6)
bTree.BSInsert(7)
bTree.BSInsert(5)
bTree.BSInsert(2)
bTree.BSInsert(1)
bTree.BSInsert(3)
bTree.InOrder() 
print(bTree.balance())
# bTree.BsDelete(4)
# bTree.InOrder()

# bTree.BsDelete(6)
# bTree.InOrder()

# bTree.BsDelete(3)
# bTree.InOrder()

# bTree.BsDelete(5)
# bTree.InOrder()

# bTree.BsDelete(7)
# bTree.InOrder()

# bTree.BsDelete(2)
# bTree.InOrder()
