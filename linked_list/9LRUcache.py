'''
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the 
key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the 
key exists. Otherwise, add the key-value pair to the cache. 
If the introduction of the new pair causes the cache to exceed its 
capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in 
O(1) average time complexity.
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    # The list always looks like this:
    #   left <-> [oldest] <-> ... <-> [newest] <-> right
    # left and right are fake "bookend" nodes that never hold real data.
    # The real node right after left is the least recently used.
    # The real node right before right is the most recently used.

    def __init__(self, capacity: int):
        self.capacity = capacity        # max number of keys allowed
        self.cache = {}                 # key -> its Node, to find any node instantly
        self.left = Node(0, 0)          # fake node at the oldest end
        self.right = Node(0, 0)         # fake node at the newest end
        self.left.next = self.right     # empty list: left points to right
        self.right.prev = self.left     # and right points back to left

    def remove(self, node: Node) -> None: # unlink node from the list
        # before <-> node <-> after   becomes   before <-> after
        before = node.prev              # the node in front of the one we're removing
        after = node.next               # the node behind the one we're removing
        before.next = after             # before now skips over node
        after.prev = before             # after now points back past node

    def insert(self, node: None) -> None:
        # before <-> right   becomes   before <-> node <-> right
        before = self.right.prev        # the current newest node (or left, if the list is empty)
        before.next = node              # old newest points forward to node
        node.prev = before              # node points back to old newest
        node.next = self.right          # node points forward to the right bookend
        self.right.prev = node          # right bookend points back to node, so node is now newest

    def get(self, key: int) -> int:
        if key not in self.cache:       # key was never added, or was evicted
            return -1

        node = self.cache[key]          # find the node instantly through the dictionary
        self.remove(node)               # take it out of its current spot
        self.insert(node)               # put it back at the newest end, since it was just used
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:           # key already exists
            self.remove(self.cache[key])  # unlink the old node, a new one replaces it below
        node = Node(key, value)         # make a node for the new value
        self.cache[key] = node          # dictionary now points to the new node
        self.insert(node)               # add it at the newest end, since it was just used

        if len(self.cache.items()) > self.capacity:  # one key too many
            lru = self.left.next        # the oldest real node sits right after left
            self.remove(lru)            # unlink it from the list
            del self.cache[lru.key]     # forget it in the dictionary too (this is why nodes store their key)



