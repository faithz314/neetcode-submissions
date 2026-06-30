# strategy: create buckets of linked lists => think malloc assignment
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [Node(0) for _ in range(10**4)] # initialize with dummy heads of 0

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]# IMPORTANT: key = key % 10k
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)