Dict_Path_Immutable
===========

Tiny Python library to modify deep dictionary properties without modifying the original dictionary (immutability).

## Install

    pip install Dict_Path_Immutable

## Quick usage

The following, sets a property without modifying the original dictionary.
It will minimize the number of clones down the line. The resulting dictionary is just a plain Python dictionary,
so be warned that it will not be protected against property mutations

```python
my_dict = {
  a: {
    b: 'c',
    c: ['d', 'f']
  }
}

new_dict = Dict_Path_Immutable.set(my_dict, 'a.b', 'f')
# {
#   a: {
#     b: 'f',
#     c: ['d', 'f']
#   }
# }
```

## API

```python
# Premises

my_dict = {
  a: {
    b: 'c',
    c: ['d', 'f']
  }
}

from Dict_Path_Immutable import Dict_Path_Immutable
```

#### get (initialDict, path)

Gets a property.

```python
nested_list = Dict_Path_Immutable.get(my_dict, 'a.c')
# [
#   'c',
#   'f'
# ]
```

```python
nested_list_item = Dict_Path_Immutable.get(my_dict, 'a.c.1')
# 'f'
```

#### set (initialDict, path, value)

Changes a dictionary property.

- Path can be either a string or an array.

```python
new_dict1 = Dict_Path_Immutable.set(my_dict, 'a.b', 'f')
new_dict2 = Dict_Path_Immutable.set(my_dict, ['a', 'b'], 'f')

# {
#   a: {
#     b: 'f',
#     c: ['d', 'f']
#   }
# }

# Note that if the path is specified as a string, numbers are automatically interpreted as array indexes.

new_dict = Dict_Path_Immutable.set(my_dict, 'a.c.1', 'fooo')
# {
#   a: {
#     b: 'f',
#     c: ['d', 'fooo']
#   }
# }
```

#### delete (initialDict, path)

Deletes a property.

```python
new_dict = Dict_Path_Immutable.delete(my_dict, 'a.c')
# {
#   a: {
#     b: 'f'
#   }
# }
```

Can also delete a deep array item using splice

```python
new_dict = Dict_Path_Immutable.delete(my_dict, 'a.c.0')
# {
#   a: {
#     b: 'f',
#     c: ['f']
#   }
# }
```