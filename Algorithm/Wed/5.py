def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                if parent:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None
                    
            # When the node has only one child
            elif nChildren == 1:
                if node.left:
                    child = node.left
                else:
                    child = node.right
                if parent:
                    if node == parent.left:
                        parent.left = child
                    else:
                        parent.right = child
     
                else:
                    self.root = child
                    
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.key = successor.key
                node.data = successor.data
           
                if successor == parent.left:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

            return True

        else:
            return False