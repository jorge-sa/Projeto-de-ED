class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, node:Node):
        if self.head == None:
            self.head = node
            self.size += 1

            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1

    def insert(self, node:Node):
        current = self.head
        if self.head == None:
            self.head = node
            self.size += 1

            return

        if (node.data.name.lower() <= current.data.name.lower()):
            node.next = current
            current.prev = node
            self.head = node
            self.size += 1
            return

        previous = None

        while (current != None) and (node.data.name.lower() >= current.data.name.lower()):
            print("Here")
            previous = current
            current = current.next

        if current == None:
            previous.next = node
            node.prev = previous
            return

        node.next = previous.next
        node.prev = current
        previous.next = current.prev = node

    def remover(self, index):
        if index < self.size:
            current = self.head

            if index == 0:
                if current.next != None:
                    current.next.prev = None
                    self.head = current.next
                else:
                    self.head = None
                
                self.size -= 1
                return current.value

            for i in range(self.size):
                if i == index:
                    current.prev.next = current.next
                    if current.next != None:
                        current.next.prev = current.prev
                    self.size -= 1

                    return current.value
                
                current = current.next
        
        raise IndexError

    def get(self, index:int):
        if index < self.size:
            current = self.head
            for i in range(self.size):
                if i == index:
                    return current.data
                
                current = current.next
        
        raise IndexError
    
    def find(self, value):
        current = self.head
        for i in range(self.size):
            if current.data.name == value:
                return i
                
            current = current.next
        
        return -1

    def printList(self):
        current = self.head
        while current != None:
            print("".join("="*50))
            current.data.show()
            #if current.next == None:
            #    print(current.prev.value, ">", current.value)
            #elif current.prev == None:
            #    print(current.value, "<", current.next.value)
            #else:
            #    print(current.prev.value, ">", current.value, "<", current.next.value)
            current = current.next

    def listSize(self):
        return self.size