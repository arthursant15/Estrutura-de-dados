from NodeTree import NodeTree

class BinaryTree: 
    def __init__(self, data=None):
        if data:
            node = NodeTree(data)
            self.root = node
        else:
            self.root = None
    
    # Percurso em ordem simétrica
    def Simetric_transversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.Simetric_transversal(node.left)
        print(node)
        if node.right:
            self.Simetric_transversal(node.right)
        print(node)
    def __str__(self):
        return str(self.data)
    
if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.right = NodeTree(10)
    tree.root.left = NodeTree(19)

    
print(tree.root)
print(tree.root.left)
print(tree.root.right)
        
