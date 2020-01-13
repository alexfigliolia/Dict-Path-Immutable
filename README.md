Object_Path_Immutable
===========

Tiny Python library to modify deep object properties without modifying the original object (immutability).

## Install

    pip install pip install Object-Path-Immutable

## Quick usage

The following, sets a property without modifying the original dictionary.
It will minimize the number of clones down the line. The resulting dictionary is just a plain Python dictionary,
so be warned that it will not be protected against property mutations

```python
dict = {
  a: {
    b: 'c',
    c: ['d', 'f']
  }
}

new_dict = Object_Path_Immutable.set(obj, 'a.b', 'f')
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

obj = {
  a: {
    b: 'c',
    c: ['d', 'f']
  }
}

from Object-Path-Immutable import Object_Path_Immutable
```

#### set (initialObject, path, value)

Changes an object property.

- Path can be either a string or an array.

```python
newObj1 = Object_Path_Immutable.set(obj, 'a.b', 'f')
newObj2 = Object_Path_Immutable.set(obj, ['a', 'b'], 'f')

# {
#   a: {
#     b: 'f',
#     c: ['d', 'f']
#   }
# }

# Note that if the path is specified as a string, numbers are automatically interpreted as array indexes.

newObj = Object_Path_Immutable.set(obj, 'a.c.1', 'fooo')
# {
#   a: {
#     b: 'f',
#     c: ['d', 'fooo']
#   }
# }
```

#### delete (initialObject, path)

Deletes a property.

```python
newObj = Object_Path_Immutable.delete(obj, 'a.c')
# {
#   a: {
#     b: 'f'
#   }
# }
```

Can also delete a deep array item using splice

```python
newObj = Object_Path_Immutable.delete(obj, 'a.c.0')
# {
#   a: {
#     b: 'f',
#     c: ['f']
#   }
# }
```