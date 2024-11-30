import json
import re
import math

# Load JSON data
with open('recipesAll.json', 'r') as file:
    recipes_data = json.load(file)

class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.parent = None
        self.next = None
        self.key = key
        self.value = value

# Scapegoat tree with chaining for prep time filter
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
    def add(self, key, value):
        new_node = Node(key, value)
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
        # Base case
        if num_of_nodes == 0:
            return None
        middle_elem = num_of_nodes // 2

        # Create the root node for this subtree
        root = arr[index + middle_elem]

        # Rebuild the left and right subtrees recursively
        root.left = self.buildBalancedFromArray(arr, index, middle_elem)
        if root.left:
            root.left.parent = root

        root.right = self.buildBalancedFromArray(arr, index + middle_elem + 1, num_of_nodes - middle_elem - 1)
        if root.right:
            root.right.parent = root

        # Rebuild the chain of duplicates
        current = root
        for i in range(index + middle_elem + 1, index + num_of_nodes):
            if arr[i].key == root.key:
                current.next = arr[i]
                arr[i].parent = root.parent  # Maintain parent consistency for chained nodes
                current = current.next
            else:
                break
        current.next = None  # Terminate the chain
        return root

    def BSTInsertAndFindDepth(self, u):
        current = self.root
        if current is None: # If the tree is empty, insert the node as the root
            self.root = u
            self.num_of_nodes += 1
            return 0
        done = False
        depth = 0
        while not done: # Traverse the tree to find the correct place for the new node
            if u.key < current.key:
                if current.left is None:
                    current.left = u
                    u.parent = current
                    done = True
                else:
                    current = current.left
            elif u.key > current.key:
                if current.right is None:
                    current.right = u
                    u.parent = current
                    done = True 
                else:
                    current = current.right
            else: # if key is the same, add the node to the chain
                if current.value == -1:
                    # Reuse the free slot by replacing the value
                    current.value = u.value
                    return -1  # Indicate that no new node was added
                elif current.next is None:
                    current.next = u
                    u.parent = current.parent
                    return -1  # Indicate that no new unique node was added
                else:
                    current = current.next
            depth += 1 # Increase depth as we go down the tree
        self.num_of_nodes += 1
        return depth
    
    def storeInArray(self, node, arr, index):
        if node is None:
            return index
        index = self.storeInArray(node.left, arr, index)

         # Add all nodes in the chain to the array
        temp = node
        while temp:  # Include all nodes in the chain
            arr[index] = temp
            index += 1
            temp = temp.next
        
        return self.storeInArray(node.right, arr, index)

    # return a list of values that have keys less than or equal than the param
    def findAndFilter(self, key):
        result = [] # Initialize the result list to store matching recipe indices
        stack = [] # Stack to simulate in-order traversal
        current = self.root
        while stack or current: # In-order traversal of the BST
            while current:
                stack.append(current)
                current = current.left
            if stack:
                current = stack.pop()
                if current.key <= key:
                    # Add all nodes in the chain (for duplicates) that match the condition
                    temp = current
                    while temp:
                        if temp.value != -1:
                            result.append(temp.value)  # Store the value (index) for each matching node
                        temp = temp.next  # Move to the next node in the chain
                if current.key > key: # If the current key is greater than the input key, no need to visit further nodes
                    break
                current = current.right # Continue with the right subtree
        return result

# create the bst and add multiples of 5 ranging from 5 - 90
prep_time_bst = SGTree()
for num in range(5,91,5):
    prep_time_bst.add(num, -1) #add -1 as temporary values 

# make prep times as the keys and indices of the json file as the values
for index, recipe in enumerate(recipes_data):
    prep_time_int = int(re.search(r'\d+', recipe['prep_time']).group()) #extracting num from string
    prep_time_bst.add(prep_time_int, index)


#`````````````for modification```````````````

# prep time filter input
filter_input = int(input("Enter time: ")) 
indices_list = prep_time_bst.findAndFilter(filter_input) #final indices list for prep time filter
print(indices_list)
#````````````````````````````````````````````