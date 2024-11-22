class Node:
    """Node class for LinkedList."""
    def __init__(self, value):
        self.value = value
        self.next = None


class PantryManager:
    def __init__(self):
        """Initialize with an empty linked list for pantry."""
        self.head = None

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
            return

        # Traverse and find the correct position
        current = self.head
        while current.next and current.next.value < ingredient:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def remove_from_pantry(self, ingredient):
        """Remove an ingredient from the pantry."""
        ingredient = ingredient.lower()

        # Empty list case
        if not self.head:
            return

        # Remove the head node if it matches
        if self.head.value == ingredient:
            self.head = self.head.next
            return

        # Traverse and remove the matching node
        current = self.head
        while current.next and current.next.value != ingredient:
            current = current.next

        if current.next:  # Found the node
            current.next = current.next.next

    def get_pantry_list(self):
        """Retrieve all ingredients in the pantry as a list."""
        pantry = []
        current = self.head
        while current:
            pantry.append(current.value.capitalize())
            current = current.next
        return pantry
