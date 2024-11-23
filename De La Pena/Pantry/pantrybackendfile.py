import json
import os

class Node:
    """Node class for LinkedList."""
    def __init__(self, value):
        self.value = value
        self.next = None


class PantryManager:
    def __init__(self):
        """Initialize with an empty linked list for pantry."""
        self.head = None
        self.load_from_json()

    @staticmethod
    def create():
        """Factory method to create an instance of PantryManager."""
        return PantryManager()

    def add_to_pantry(self, ingredient):
        """Add an ingredient to the pantry in sorted order."""
        ingredient = ingredient.lower()
        new_node = Node(ingredient)

        # Insert at the beginning or as the head
        if self.head is None or self.head.value >= ingredient:
            new_node.next = self.head
            self.head = new_node
            self.save_to_json()  # Save to JSON after adding
            return

        # Traverse and find the correct position
        current = self.head
        while current.next and current.next.value < ingredient:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.save_to_json()  # Save to JSON after adding

    def remove_from_pantry(self, ingredient):
        """Remove an ingredient from the pantry."""
        ingredient = ingredient.lower()

        # Empty list case
        if not self.head:
            return

        # Remove the head node if it matches
        if self.head.value == ingredient:
            self.head = self.head.next
            self.save_to_json()  # Save to JSON after removing
            return

        # Traverse and remove the matching node
        current = self.head
        while current.next and current.next.value != ingredient:
            current = current.next

        if current.next:  # Found the node
            current.next = current.next.next
            self.save_to_json()  # Save to JSON after removing

    def get_pantry_list(self):
        """Retrieve all ingredients in the pantry as a list."""
        pantry = []
        current = self.head
        while current:
            pantry.append(current.value.capitalize())
            current = current.next
        return pantry

    def load_from_json(self):
        """Load the pantry list from the JSON file."""
        if os.path.exists("pantry.json"):
            with open("pantry.json", "r") as file:
                pantry_data = json.load(file)
                # Populate the linked list from the JSON data
                for ingredient in pantry_data:
                    self.add_to_pantry(ingredient)  # Will automatically add in sorted order

    def save_to_json(self):
        """Save the pantry list to the JSON file."""
        pantry_data = self.get_pantry_list()
        with open("pantry.json", "w") as file:
            json.dump(pantry_data, file, indent=4)
