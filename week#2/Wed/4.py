class Node:

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key,data)
            else:
                self.left = Node(key,data)
        elif key > self.key:
            if self.right:
                self.right.insert(key,data)
            else:
                self.right = Node(key,data)
        else:
            raise KeyError("중복된 값이 존재합니다.")


class BinSearchTree:

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)