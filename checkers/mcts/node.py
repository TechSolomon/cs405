class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        if self.next is None:
            self.next = Node(data)
        else:
            self.next.append(data)
