import json
import re
import math

# Load JSON data
with open('recipesAll.json', 'r') as file:
    recipes_data = json.load(file)

class Node:
    def __init__(self, value = 0):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

# Scapegoat tree for prep time filter
class SGTree:
    def __init__(self):
        self.root = None
        self.num_of_nodes = 0

    # Get the size of the subtree rooted at a given node
    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
    
    # add a new node into the tree
    def add(self, x):
        new_node = Node(x)
        depth = self.BSTInsertAndFindDepth(new_node) #insert node into the tree and get its depth
        if depth > math.ceil(2.4663034623764317 * math.log(self.num_of_nodes, 3)): #check if tree is unbalanced
            parent = new_node.parent
            while 3 * self.size(parent) <= 2 * self.size(parent.parent): #find the root of the subtree to be rebuilt
                parent = parent.parent
            self.rebuildTree(parent.parent) #rebuild subtree
        return depth >= 0

    def rebuildTree(self, u):
        num_of_nodes = self.size(u) #find the number of nodes in the subtree rooted at u
        parent = u.parent #get u's parent
        arr = [None] * num_of_nodes #create an array of size num_of_nodes
        self.storeInArray(u, arr, 0) #fill arr w/ nodes from the subtree rooted at u
        if parent is None:
            #if u is the root of the tree, build a balanced tree from arr
            self.root = self.buildBalancedFromArray(arr, 0, num_of_nodes)
            self.root.parent = None
        elif parent.right == u:
            #if u is the right child of its parent, build a balanced tree from arr
            #and make it the new right child of parent
            parent.right = self.buildBalancedFromArray(arr, 0, num_of_nodes)
            parent.right.parent = parent
        else:
            #if u is the left child of its parent, build a balanced tree from arr
            #and make it the new left child of parent
            parent.left = self.buildBalancedFromArray(arr, 0, num_of_nodes)
            parent.left.parent = parent

    def buildBalancedFromArray(self, arr, index, num_of_nodes):
        #base case
        if num_of_nodes == 0:
            return None
        middle_elem = num_of_nodes // 2 #find the middle element of arr

        #create a node for the middle element and recursively build balance BST's
        #from the left and right halves of the array
        arr[index + middle_elem].left = self.buildBalancedFromArray(arr, index, middle_elem)
        if arr[index + middle_elem].left is not None:
            arr[index + middle_elem].left.parent = arr[index + middle_elem]

        arr[index + middle_elem].right = self.buildBalancedFromArray(arr, index+middle_elem+1, num_of_nodes-middle_elem-1)
        if arr[index + middle_elem].right is not None:
            arr[index + middle_elem].right.parent = arr[index + middle_elem]

        return arr[index + middle_elem] #return the root of the balanced BST
    
    def BSTInsertAndFindDepth(self, u):
        current = self.root
        if current is None: # If the tree is empty, insert the node as the root
            self.root = u
            self.num_of_nodes += 1
            return 0
        done = False
        depth = 0
        while not done: # Traverse the tree to find the correct place for the new node
            if u.value < current.value:
                if current.left is None:
                    current.left = u
                    u.parent = current
                    done = True
                else:
                    current = current.left
            elif u.value > current.value:
                if current.right is None:
                    current.right = u
                    u.parent = current
                    done = True
                else:
                    current = current.right
            else:
                return -1 # Value already exists
            depth += 1 # Increase depth as we go down the tree
        self.num_of_nodes += 1
        return depth
    
    def storeInArray(self, node, arr, index):
        if node is None:
            return index
        index = self.storeInArray(node.left, arr, index)
        arr[index] = node
        index += 1
        return self.storeInArray(node.right, arr, index)

    # return a list of values that are less than or equal to the param
    def filter(self, value):
        result = []
        stack = []
        current = self.root

        while stack or current:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Process the node
            current = stack.pop()
            if current.value <= value:
                result.append(current.value)
            else:
                break
            current = current.right # Move to the right child
        return result

# create the bst and add multiples of 5 ranging from 5 - 90
prep_time_bst = SGTree()
for num in range(5,91,5):
    prep_time_bst.add(num)

# create a list of prep_times from the json file
prep_times = []
for index, recipe in enumerate(recipes_data):
    prep_time_int = int(re.search(r'\d+', recipe['prep_time']).group()) #extracting num from string
    prep_times.append(prep_time_int)

# add the prep_times in the bst
for num in prep_times:
    prep_time_bst.add(num)

#`````````````for modification```````````````

# prep_time filter input
filter_input = int(input("Enter time: ")) 
filtered_list = prep_time_bst.filter(filter_input)
#````````````````````````````````````````````

# return a list of indices of the filtered recipes based on the json file
indices_list = [] #final indices list for prep time filter
for num in filtered_list:
    for index, recipe in enumerate(recipes_data):
        prep_time_int = int(re.search(r'\d+', recipe['prep_time']).group()) #extracting num from string
        if prep_time_int == num:
            indices_list.append(index)


#`````````````for modification```````````````
print(indices_list) # the order of the list is in increasing prep time 