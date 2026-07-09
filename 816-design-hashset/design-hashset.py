class MyHashSet(object):

    def __init__(self):
        self.data = set()

    def add(self, key):
        self.data.add(key)



    def remove(self, key):
        self.data.discard(key)        

    def contains(self, key):
        return key in self.data
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)