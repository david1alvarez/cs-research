class HashTable(object):
    def __init__(self, length=4):
        self.array = [None] * length
        self.currentIndex = [0, 0]

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        for item in self.array:
            if item is not None:
                for kvp in list(item):
                    if kvp[0] == key:
                        return True
        else:
            return False
    
    def __iter__(self):
        return self
                
    def __next__(self):
        while self.currentIndex[0] < len(self.array):
            if self.array[self.currentIndex[0]] is not None:
                # print('for index '+str(self.currentIndex[0])+': '+str(self.array[self.currentIndex[0]]))
                while self.currentIndex[1] < len(self.array[self.currentIndex[0]]):
                    item = self.array[self.currentIndex[0]][self.currentIndex[1]]
                    self.currentIndex[1] += 1
                    return item
                self.currentIndex[1] = 0
            self.currentIndex[0] += 1
        
        raise StopIteration



    def hash(self, key):
        """Get the index of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        """Add a value to the array by its key"""
        index = self.hash(key)
        if self.array[index] is not None: # key hash collision
            for kvp in self.array[index]:
                if kvp[0] == key: # update key if found
                    kvp[1] = value
                    break
            else: # if the collision isn't due to a previously used key
                self.array[index].append([key, value])
        else: # unused hash, add kvp to array
            self.array[index] = []
            self.array[index].append([key, value])

        if self.isFull():
            self.double()
    
    def get(self, key):
        """Get value by key"""
        index = self.hash(key)
        if self.array[index] is None: # if no key match found, raise error
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            
            raise KeyError() # if no key match found, raise error

    def isFull(self):
        """Determine if the hash table is full"""
        items = 0
        for item in self.array:
            if item is not None:
                items += 1

        return items > len(self.array)/2

    def double(self):
        """Double the list and re-add the values"""
        ht2 = HashTable(length=len(self.array)*2)

        for i in range(len(self.array)):
            if self.array[i] == None:
                continue

            for kvp in self.array[i]:
                ht2.add(kvp[0], kvp[1])
        
        self.array = ht2.array


ht = HashTable()
ht.add('1', 1)
ht['2'] = 2
ht.add('3', 3)
ht.add('4', 4)
ht.add('5', 5)
ht.add('6', 6)
ht.add('7', 7)
ht.add('8', 8)
ht.add('9', 9)
ht.add('10', 10)
ht.add('11', 11)
ht.add('12', 12)

print(ht['2'])
if "2" in ht:
    print("exists")

for kvp in ht:
    print(kvp)
