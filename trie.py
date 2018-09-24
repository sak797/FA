# From https://www.geeksforgeeks.org/trie-insert-and-search/
# and https://www.geeksforgeeks.org/trie-delete/

class trienode():
    def __init__(self):
        self.children = [None] * 26
        self.value = 0

    def isleaf(self):
        return self.value != 0

    def isFree(self):
        for child in self.children:
            if child:
                return False
        return True

class trie():
    def __init__(self):
        self.root = trienode()
        self.count = 0

    def chartoind(self, val):
        return ord(val) - ord('a')

    def insert(self, key):
        start = self.root
        self.count += 1
        for char in range(len(key)):
            index = self.chartoind(key[char])
            if not start.children[index]:
                start.children[index] = trienode()
            start = start.children[index]
        start.value = self.count

    def search(self, key):
        start = self.root
        for char in range(len(key)):
            index = self.chartoind(key[char])
            if not start.children[index]:
                return False
            start = start.children[index]
        return start != None and start.isleaf()

    def delete(self,key):
        start = self.root
        if len(key):
            self.delete_helper(start, key, 0 , len(key))

    def delete_helper(self,start, key, level, length):
        if start:
            if level == length:
                if start.value:
                    start.value = 0
                return start.isFree()
            else:
                index = self.chartoind(key[level])
                if self.delete_helper(start.children[index], key, level + 1, length):
                    del start.children[index]
                    return not start.isleaf() and start.isFree()
        return False


if __name__ == '__main__':
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie",
              "Present in tire"]
    t = trie()
    for key in keys:
        t.insert(key)
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))
    t.delete(keys[0])
    print("{} ---- {}".format("the", output[t.search("the")]))
