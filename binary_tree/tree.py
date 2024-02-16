
from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

    def pre_order(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.post_order(root.right)
            self.post_order(root.left)

    def adjancent_list(self, root, d: dict = {}):
        if root is not None:
            d[root.data] = []
            self.adjancent_list(root.left, d)

            if root.left:
                d[root.data].append(root.left.data)

            if root.right:
                d[root.data].append(root.right.data)

            self.adjancent_list(root.right, d)
        
        return d
    
    def breadth_first_search(self, adjancent_list: dict):
        queue = deque("g")
        visited = []

        while queue:
            node = queue.popleft()
            visited.append(node)
            [queue.append(value) for value in adjancent_list[node]]

        print(visited)

