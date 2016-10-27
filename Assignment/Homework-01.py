**`A:`** What would Python print?
```python
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
Print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]
```

**`B:`** Write a function that removes all instances of an element from a list.
```python
"""Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
"""
def removeAll(elem,lst):
  while elem in lst:
    lst.remove (elem)    
alpha = [1,9,3,7,4,9,3,9]
removeAll(9, alpha)print (alpha)

```
**`C:`** Write a function that takes in two values, x and y, and a list, and adds as many y's to
the end of the list as there are x's. Do not use the built-in function count.

```python
""" Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
"""
def add_this_values(x, y, list):
  for elem in list:
    if elem == x:
    	list.append (y)
        
vic = [2, 2, 6, 3, 2, 1, 2, 5]
print('list before', vic)

add_this_values(2, 6,vic)
print('list after', vic)

```
**`D:`**  What would Python print?

```python
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]
```

**`E:`**  Let's reverse Python lists in place, meaning mutate the passed in list itself, instead of returning a new list.
We didn't discuss this in class directly, so feel free to use google. Why is the "in place" solution preferred?

```python
""" Reverses lst in place. 
Given: x = [3, 2, 4, 5, 1] 
Usage: reverse(x)
Results: [1, 5, 4, 2, 3]
"""
import math
def reverse (lst):
	for el in range (0, math.ceil(len(lst)/2)):
		lst[el], lst[len(lst)-1-el] = lst [len(lst)-1-el], lst[el]
		
v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse(v)
print(v)   
#prints: [9, 8, 7, 6, 5, 4, 3, 2, 1]

```
**`F.`** Write a function that rotates the elements of a list to the right by `k`. Elements should not ”fall off”; they should wrap around the beginning of the list. `rotate` should return a new list. To make a list of `n` `0's`,you can do this: `[0] * n`

```python
""" Return a new list, with the same elements of lst, rotated to the right k.
Given: x = [1, 2, 3, 4, 5]
Usage: rotate(x, 3)
Results: [3, 4, 5, 1, 2]
"""
def rotate(lst, k):
	L = []
	for i in range(len(lst)):
		i -= 1
		
		L.insert(len(L),lst[i])
	print(L)

x = [1, 2, 3, 4, 5]

rotate(x, 1)
```

**`H:`**  Continuing from above, what would Python print?

```python
print('colin kaepernick' in superbowls)
#Prints: false

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: false

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'joe flacco': 1, 'peyton manning': 1, ('eli manning', 'giants'): 2, 'joe montana': 4, 'tom brady': 3}


superbowls[3] = 'cat'
print(superbowls)
#Prints: {'joe flacco': 1, 'peyton manning': 1, 3: 'cat', 'joe montana': 4, 'tom brady': 3, ('eli manning', 'giants'): 2}


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {'joe flacco': 1, 'peyton manning': 1, 3: 'cat', 'joe montana': 4, 'tom brady': 3, ('eli manning', 'giants'): 5}


superbowls[['steelers', '49ers']] = 11
print(superbowls)
#Prints: TypeError: unhashable type: 'list'
   
```
**`I:`**  Given a dictionary replace all occurrences of x as the value with y.

```python
def replace_all(d, x, y):
"""Replaces all values of x with y. 
Given: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}} 
Usage: replace_all(d,3,1)
Results: {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}} 
"""
def replace_all(d, x, y):
	for k in d.keys():
		if d[k] == x:
			d[k] = y
			
		
dict = {'bob': 2, 'sam': 4, 'sue': 5, 'jun': 3, 'fred': 2}
print (dict)

replace_all(dict, 2, 9)
print(dict)


```

**`J:`**  Given a (non-nested) dictionary delete all occurences of a value. You cannot delete items in a dictionary as you are iterating through it (google :) ).

 ```python
def rm(d, x):
"""Removes all pairs with value x. 
Given:  d = {1:2, 2:3, 3:2, 4:3}
Usage:  rm(d,2)
Results: {2:3, 4:3}
"""
def rmove(d, rm):
	d = {k:v for k, v in d.items() if not v ==rm}
	print(d)
			
d = {'bob': 2, 'sam': 4, 'sue': 5, 'jun': 3, 'fred': 2, 2:'bob'}

rmove(d, 2) 
#prints: {'jun': 3, 2: 'bob', 'sue': 5, 'sam': 4}

```


















