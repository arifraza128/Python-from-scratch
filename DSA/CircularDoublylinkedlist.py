class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        tail = self.head.prev

        tail.next = new_node
        new_node.prev = tail

        new_node.next = self.head
        self.head.prev = new_node

    def display(self):
        if self.head is None:
            return

        temp = self.head

        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")

cdll = CircularDoublyLinkedList()

cdll.insert(10)
cdll.insert(20)
cdll.insert(30)

cdll.display()
