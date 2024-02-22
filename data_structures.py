class DataProcessor:
    def __init__(self):
        # Initialize an empty dictionary
        self.data_dict = {}

    def add_element(self, key, value):
        """
        Add an element to the dictionary.
        """
        self.data_dict[key] = value

    def remove_element(self, key):
        """
        Remove an element from the dictionary.
        """
        if key in self.data_dict:
            del self.data_dict[key]
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def update_element(self, key, new_value):
        """
        Update the value of an existing element in the dictionary.
        """
        if key in self.data_dict:
            self.data_dict[key] = new_value
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def sort_elements(self):
        """
        Sort the dictionary by keys and return a sorted list of key-value pairs.
        """
        sorted_items = sorted(self.data_dict.items())
        return sorted_items

    def display_elements(self):
        """
        Display all elements in the dictionary.
        """
        for key, value in self.data_dict.items():
            print(f"{key}: {value}")

# Example usage
processor = DataProcessor()

# Add elements
processor.add_element("apple", 5)
processor.add_element("banana", 3)
processor.add_element("cherry", 8)

# Display elements
print("Initial dictionary:")
processor.display_elements()

# Update an element
processor.update_element("banana", 6)

# Sort elements
sorted_items = processor.sort_elements()
print("\nSorted dictionary:")
for key, value in sorted_items:
    print(f"{key}: {value}")

# Remove an element
processor.remove_element("cherry")

# Display updated elements
print("\nUpdated dictionary:")
processor.display_elements()
