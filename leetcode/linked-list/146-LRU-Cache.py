class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.mpp = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prevnode = node.prev
        nextnode = node.next

        prevnode.next = nextnode
        nextnode.prev = prevnode

    def insert(self, node):
        nextnode = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = nextnode
        nextnode.prev = node

    def get(self, key):
        if key not in self.mpp:
            return -1

        node = self.mpp[key]

        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key, value):
        if key in self.mpp:
            node = self.mpp[key]
            node.val = value

            self.remove(node)
            self.insert(node)

        else:
            if len(self.mpp) == self.cap:
                lru = self.tail.prev
                self.remove(lru)
                del self.mpp[lru.key]

            newnode = Node(key, value)
            self.insert(newnode)
            self.mpp[key] = newnode

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)