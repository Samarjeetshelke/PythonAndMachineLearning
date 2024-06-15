Sure, here is an example of how to use the built-in Python `filter` function to filter data:

```python
# Example list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to filter even numbers
def is_even(number):
    return number % 2 == 0

# Using filter function to get even numbers
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list to see the results
even_numbers_list = list(even_numbers)

print("Original list:", numbers)
print("Filtered list (even numbers):", even_numbers_list)
```

In this example:
- `is_even` is a function that returns `True` if a number is even.
- `filter(is_even, numbers)` applies this function to each element in the `numbers` list and returns an iterator with only the elements for which the function returned `True`.
- `list(even_numbers)` converts the filter object to a list so you can easily see the results.

You can use the `filter` function with any custom filtering logic by defining an appropriate function. Here is another example with a list of dictionaries:

```python
# Example list of dictionaries
people = [
    {'name': 'Alice', 'age': 24},
    {'name': 'Bob', 'age': 27},
    {'name': 'Charlie', 'age': 22},
    {'name': 'David', 'age': 32},
    {'name': 'Eve', 'age': 29}
]

# Function to filter people older than 25
def is_older_than_25(person):
    return person['age'] > 25

# Using filter function to get people older than 25
filtered_people = filter(is_older_than_25, people)

# Convert the filter object to a list to see the results
filtered_people_list = list(filtered_people)

print("Original list of people:", people)
print("Filtered list (age > 25):", filtered_people_list)
```

In this example:
- `is_older_than_25` is a function that returns `True` if the person's age is greater than 25.
- `filter(is_older_than_25, people)` applies this function to each dictionary in the `people` list and returns an iterator with only the dictionaries for which the function returned `True`.
- `list(filtered_people)` converts the filter object to a list so you can see the results.

This demonstrates the flexibility and power of the `filter` function in Python.


```python

lis = [1,3,4,5,6,7]

data = list(filter(lambda x: x==3,lis))

print(data)

data = list(filter(lambda x: x%2==0,lis))

print(data)

data = list(filter(lambda x: x%2!=0,lis))

print(data)
