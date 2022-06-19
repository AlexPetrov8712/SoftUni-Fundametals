method = input()
if method == 'split':
    print('Optional. Specifies the separator to use when splitting the string. By default any whitespace /'
          'is a separator')
elif method == 'append':
    print('The append() method appends an element to the end of the list.')
elif method == 'remove':
    print('The remove() method removes the first occurrence of the element with the specified value.')
elif method == 'clear':
    print('The clear() method removes all the elements from a list.')
elif method == 'copy':
    print('The copy() method returns a copy of the specified list.')
elif method == 'count':
    print('The count() method returns the number of elements with the specified value.')
elif method == 'extend':
    print('The extend() method adds the specified list elements (or any iterable) to the end of the current list.')
elif method == 'index':
    print('The index() method returns the position at the first occurrence of the specified value.')
elif method == 'insert':
    print('The insert() method inserts the specified value at the specified position.')
elif method == 'pop':
    print('The pop() method removes the element at the specified position.')
elif method == 'reverse':
    print('The reverse() method reverses the sorting order of the elements.')
elif method == 'sort':
    print('The sort() method sorts the list ascending by default.'
          'You can also make a function to decide the sorting criteria(s).')
elif method == 'min':
    print('The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.'
          'If the values are strings, an alphabetically comparison is done.')
elif method == 'max':
    print(
        'The max() function returns the item with the highest value, or the item with the highest value in an iterable.'
        'If the values are strings, an alphabetically comparison is done.')
elif method == 'all':
    print('The all() function returns True if all items in an iterable are true, otherwise it returns False.'
          'If the iterable object is empty, the all() function also returns True.')
elif method == 'join':
    print('The join() method takes all items in an iterable and joins them into one string.'
          'A string must be specified as the separator.')
elif method == 'filer':
    print('The filter() function returns an iterator were the items are filtered through a'
          'function to test if the item is accepted or not.')
