class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class SLL:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def append(self, data):
        NewNode = Node(data)
        if self.isEmpty():
            self.__head = NewNode
        else:
            trav = self.__head
            while trav.next:
                trav = trav.next
            trav.next = NewNode
        self.__size += 1

    def prepend(self, data):
        NewNode = Node(data, self.__head)
        self.__head = NewNode
        self.__size += 1

    def addAt(self, index, data):
        if index < 0 or index > self.size():
            raise Exception("Invalid Index")
        if index == 0:
            self.prepend(data)
        else:
            trav = self.__head
            for _ in range(index - 1):
                trav = trav.next
            NewNode = Node(data, trav.next)
            trav.next = NewNode
            self.__size += 1

    def removeAt(self, index):
        if index < 0 or index >= self.size():
            raise Exception("Invalid Index")
        if index == 0:
            temp = self.__head
            self.__head = self.__head.next
            del temp
        else:
            trav = self.__head
            for _ in range(index - 1):
                trav = trav.next
            temp = trav.next
            trav.next = trav.next.next
            del temp
        self.__size -= 1


    def reverse(self):
        prev = None
        current = self.__head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev

    def merge(self, other):
        if self.isEmpty():
            self.__head = other.__head
        elif not other.isEmpty():
            trav = self.__head
            while trav.next:
                trav = trav.next
            trav.next = other.__head
        self.__size += other.__size


    def middle(self):
        if self.isEmpty():
            return None
        slow = fast = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def indexOf(self, data):
        trav = self.__head
        index = 0
        while trav:
            if trav.data == data:
                return index
            trav = trav.next
            index += 1
        return -1

    def split(self, index):
        if index < 0 or index >= self.size():
            raise Exception("Invalid Index")
        if index == 0:
            new_list = SLL()
            new_list.__head = self.__head
            new_list.__size = self.__size
            self.__head = None
            self.__size = 0
            return new_list
        trav = self.__head
        for _ in range(index - 1):
            trav = trav.next
        new_list = SLL()
        new_list.__head = trav.next
        new_list.__size = self.__size - index
        trav.next = None
        self.__size = index
        return new_list

    def __str__(self):
        l = []
        trav = self.__head
        while trav is not None:
            l.append(trav.data)
            trav = trav.next
        return '->'.join(map(str, l))
