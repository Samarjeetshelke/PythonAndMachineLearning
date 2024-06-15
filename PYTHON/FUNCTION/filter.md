Sure! You can use a lambda expression with the `filter` function to filter out words from a list that don't start with the letter 's'. Here is how you can do it:

```python
# List of words
seq = ['soup', 'dog', 'salad', 'cat', 'great']

# Use filter with a lambda function to filter words that start with 's'
filtered_words = list(filter(lambda word: word.startswith('s'), seq))

# Print the filtered list
print(filtered_words)
```

### Explanation:
- The `filter` function takes two arguments: a function and an iterable. It applies the function to each item in the iterable and includes the item in the result if the function returns `True`.
- The lambda function `lambda word: word.startswith('s')` returns `True` if a word starts with the letter 's'.
- `list(filter(...))` converts the filter object to a list.

### Example Output:
```
['soup', 'salad']
```

This code will correctly filter the list and return only the words that start with the letter 's'.



Certainly! To filter out words from a list that **do not** start with the letter 's', you can modify the lambda function accordingly:

```python
# List of words
seq = ['soup', 'dog', 'salad', 'cat', 'great']

# Use filter with a lambda function to filter out words that do not start with 's'
filtered_words = list(filter(lambda word: not word.startswith('s'), seq))

# Print the filtered list
print(filtered_words)
```

### Explanation:
- The `filter` function takes a lambda function and a list.
- The lambda function `lambda word: not word.startswith('s')` returns `True` if the word does not start with the letter 's'.
- `list(filter(...))` converts the filter object to a list.

### Example Output:
```
['dog', 'cat', 'great']
```

This code will correctly filter the list and return only the words that do not start with the letter 's'.
