from config import recipes_data

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# modified hash table using chaining for difficulty filter
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.size = 0 
        self.table = [None] * capacity

    # hash function
    def _hash(self, key):
        if key == 'Easy':
            return 0
        elif key == 'Moderate':
            return 1
        elif key == 'Intermediate':
            return 2
        elif key == 'Advanced':
            return 3
        elif key == 'Expert':
            return 4

    def add(self, key, value):
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

    #takes advantage of collision, all values sharing the same key are accessed 
    def findAndFilter(self, key):
        index = self._hash(key)
        indices_list = [] 
        current = self.table[index]
        while current:
            indices_list.append(current.value)
            current = current.next
        return indices_list #returns an indices list according to difficulty level


class DifficultyFilter:
    def __init__(self):
        #create the hash table
        self.hashTable = HashTable(5) 
        self.initTable()

    def initTable(self):
        # make difficulty as the keys and indices of the json file as the values
        for index in range(len(recipes_data)): #iterate through the file and add elements to the table
            self.hashTable.add(recipes_data[index]["difficulty"], index)

    def filter(self, filterList):
        finalIndexList = []
        for filterItem in filterList: #obtain all the active filters
            #filter and append all the obtained recipe for each filter into new list
            finalIndexList.append(self.hashTable.findAndFilter(filterItem))

        #convert the indices into the processnames
        #it is a list of lists so we use nested for loop
        obtainedNamesList = []
        for typeList in finalIndexList:
            for item in typeList:
                obtainedNamesList.append(recipes_data[item]["preprocessedname"])

        return obtainedNamesList        
