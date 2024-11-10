# Set - {} a collection used to store unique data elements, no duplicates allowed
example = {1, 2, 2, 3, 3}  # Duplicate elements are automatically removed
print(example)  # Output the set

# Removing an element from the set; can also use discard() or pop() to remove the first element
example.remove(3)  
print(5 in example)  # Check if 5 is present in the set (will return False)

# Updating the set by adding new elements
example.update([4, 5])
print(example)  # Output the updated set
print(5 in example)  # Check if 5 is now present in the set (will return True)



