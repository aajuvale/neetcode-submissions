class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashMap = {} #make this of size capacity

        #Left = Least recently used, right = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    #remove values from the list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        
        #changing the pointers so that they no longer point to the extra values
        prev.next = nxt
        nxt.prev = prev
    
    #insert on the right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.hashMap:
            # Update to most recent
            self.remove(self.hashMap[key])
            self.insert(self.hashMap[key])
            return self.hashMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if len(self.hashMap) < self.capacity - 1:
        #     print(len(self.hashMap))
        #     self.hashMap[key] = value
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        self.hashMap[key] = Node(key, value)
        self.insert(self.hashMap[key])
        if len(self.hashMap) > self.cap:
            # remove the doubly linked list and delete the least recently used from the hashmap       
            lru = self.left.next
            self.remove(lru)
            del self.hashMap[lru.key]