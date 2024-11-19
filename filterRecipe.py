import json
from binarytree import Node

# Load JSON data
with open('recipesAll.json', 'r') as file:
    recipes_data = json.load(file)

class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.value} (Prep time: {self.key} minutes)"

class BSTNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.values = []

    def add_value(self, value):
        self.values.append(value)

    def __repr__(self):
        return f"Key: {self.value}, Values: {self.values}"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, keyvalue):
        if self.root is None:
            self.root = BSTNode(keyvalue.key)
            self.root.add_value(keyvalue)
        else:
            self._insert(self.root, keyvalue)

    def _insert(self, node, keyvalue):
        if keyvalue.key < node.value:
            if node.left is None:
                node.left = BSTNode(keyvalue.key)
                node.left.add_value(keyvalue)
            else:
                self._insert(node.left, keyvalue)
        elif keyvalue.key > node.value:
            if node.right is None:
                node.right = BSTNode(keyvalue.key)
                node.right.add_value(keyvalue)
            else:
                self._insert(node.right, keyvalue)
        else:
            node.add_value(keyvalue)  # Add to list for duplicate keys

    def inorder(self):
        def _inorder(node):
            return _inorder(node.left) + [node] + _inorder(node.right) if node else []
        return _inorder(self.root)

    def find(self, key):
        def _find(node, key):
            if node is None:
                return None
            if key == node.value:
                return node.values
            elif key < node.value:
                return _find(node.left, key)
            else:
                return _find(node.right, key)
        return _find(self.root, key)

def createListOfNodes(recipes_data):
    if not recipes_data:
        return []
    nodes = []
    for recipe in recipes_data:
        prep_time = int(recipe["prep_time"].split()[0]) # extract numeric value of minutes
        recipe_name = recipe["name"]
        pair = KeyValuePair(prep_time, recipe_name)
        nodes.append(pair)
    return nodes

nodes = createListOfNodes(recipes_data)

# Initialize BST and insert data
bst = BST()
for kvp in nodes:
    bst.insert(kvp)

# Print the BST in order
for node in bst.inorder():
    print(node)

# Optional: visualize using binarytree
binary_tree_root = bst.root
print(binary_tree_root)

# Access values based on the key
key_to_find = 25  # Example key (prep time)
found_values = bst.find(key_to_find)
if found_values:
    for value in found_values:
        print(f"Found recipe: {value}")
else:
    print(f"No recipe found with prep time {key_to_find} minutes.")
