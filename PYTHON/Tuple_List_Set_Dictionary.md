In Python, tuples, lists, sets, and dictionaries are all built-in data structures, each with its own properties and use cases. Here's a comparison of each, including their properties, use cases, and examples:

### 1. Tuple

**Properties:**
- Immutable: Once created, the elements cannot be changed.
- Ordered: Elements have a defined order and can be accessed by index.
- Allows duplicate elements.
- Can contain mixed data types.

**Use Cases:**
- Storing related items that should not change.
- Returning multiple values from a function.
- Using as keys in dictionaries (since they are hashable).

**Example:**
```python
# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple[1])  # Output: 2

# Function returning multiple values as a tuple
def get_point():
    return (1, 2)
x, y = get_point()
print(x, y)  # Output: 1 2
```

### 2. List

**Properties:**
- Mutable: Elements can be changed, added, or removed.
- Ordered: Elements have a defined order and can be accessed by index.
- Allows duplicate elements.
- Can contain mixed data types.

**Use Cases:**
- Storing collections of items that may need to change.
- Performing operations like sorting, appending, or modifying elements.

**Example:**
```python
# Creating a list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Modifying an element
my_list[1] = 10
print(my_list)  # Output: [1, 10, 3, 4]
```

### 3. Set

**Properties:**
- Mutable: Elements can be added or removed.
- Unordered: No defined order, and elements cannot be accessed by index.
- Does not allow duplicate elements.
- Can only contain hashable (immutable) items.

**Use Cases:**
- Storing unique items.
- Performing mathematical set operations like union, intersection, and difference.
- Checking membership quickly.

**Example:**
```python
# Creating a set
my_set = {1, 2, 3, 3}
print(my_set)  # Output: {1, 2, 3}

# Adding an element
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Set operations
another_set = {3, 4, 5}
print(my_set & another_set)  # Output: {3, 4} (intersection)
```

### 4. Dictionary

**Properties:**
- Mutable: Entries can be added, changed, or removed.
- Unordered (in Python 3.7+ dictionaries maintain insertion order).
- Key-value pairs: Keys must be unique and hashable, values can be of any type.
- Fast lookups by key.

**Use Cases:**
- Storing data pairs (like a mapping from keys to values).
- Fast lookups, insertions, and deletions by key.
- Implementing associative arrays or hash maps.

**Example:**
```python
# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['b'])  # Output: 2

# Adding and modifying entries
my_dict['d'] = 4
my_dict['a'] = 10
print(my_dict)  # Output: {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# a: 10
# b: 2
# c: 3
# d: 4
```

### Summary

- **Tuple:** Immutable, ordered, allows duplicates, can contain mixed data types. Use for fixed collections of items.
- **List:** Mutable, ordered, allows duplicates, can contain mixed data types. Use for collections of items that need to change.
- **Set:** Mutable, unordered, no duplicates, elements must be hashable. Use for unique items and set operations.
- **Dictionary:** Mutable, unordered (insertion order in Python 3.7+), key-value pairs, keys must be unique and hashable. Use for mapping and fast lookups by key.
