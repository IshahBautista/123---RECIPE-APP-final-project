from config import json_path, recipes_data

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# modified hash table using chaining for origin filter
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.load_factor = 0.7
        self.hashlist = []

    # hash function
    def _hash(self, key):
        return hash(key) % self.capacity

    def add(self, key, value):
        if self.size / self.capacity > self.load_factor:
            self._resize() 

        index = self._hash(key)
        if self.table[index] is None:             # if true, create a new node with the key-value and
            self.table[index] = Node(key, value)  # and set it as the head of the list
            self.size += 1                       
        else:
            current = self.table[index]
            while current.next:  # iterate through the list till the last node is found 
                current = current.next
            current.next = Node(key, value) #create a new node and add it to the singly linked list
            self.size += 1

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0 # Reset size, it will be recalculated during rehashing

        for head in old_table:
            current = head
            while current:
                self.add(current.key, current.value)
                current = current.next

    #takes advantage of collision, all values sharing the same key are accessed 
    def findAndFilter(self, key):
        index = self._hash(key)
        indices_list = [] 
        current = self.table[index]
        while current:
            indices_list.append(current.value)
            current = current.next
        return indices_list #returns an indices list according to origin


class OriginFilter:
    def __init__(self):
        #create the hash table
        self.hashTable = HashTable(30) 
        self.initTable()

    def initTable(self):
        # make origins as the keys and indices of the json file as the values
        for index in range(len(recipes_data)): #iterate through the file and add elements to the table
            self.hashTable.add(recipes_data[index]["origin"], index)

    def filter(self, filterList):
        finalIndexList = []
        for filterItem in filterList:
            finalIndexList.append(self.hashTable.findAndFilter(filterItem))

        obtainedNamesList = []

        for typeList in finalIndexList:
            for item in typeList:
                obtainedNamesList.append(recipes_data[item]["preprocessedname"])

        return obtainedNamesList         

