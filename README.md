# 100 Days Of Python
Here is my practices for [100 Days of Code: The Complete Python Pro Bootcamp for 2022](https://100daysofpython.dev/)

## Tools
- Replit: A free browser-based code editor.

## Coding Style
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## Data Type
In Java terms, there are no primitive data types in Python. Everything is an object.

### Built-in Data Types
`type(variable)` : check data type for a `variable`.
- Numbers: int / float / complex
  - `random()` : Make a random number.
- Boolean (True / False)
  - `bool()` : evaluate any value to return True or False.
  - False: empty string, number 0, empty list, tuple, set, and dictionary.
- String
  - f-string: string formatting. `print(f"your score is {score}, your height is {height}")`

There are four collection data types in the Python:
### List
List items are ordered, changeable, and allow duplicate values, different data types.
```
# Constructor
thislist = list(("apple", "banana", "cherry"))
emptylist = list()
test = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Access
print(test[1]) # banana
print(test[-1]) # mango
print(test[2:5]) # ['cherry', 'orange', 'kiwi'] NOT include the last index!

# Update
test[1] = "blackcurrant"

# Add
test.append("pomelo")
test.insert(1, "orange")

# Remove
test.remove("banana") # returns None. Throws ValueError exception when element doesn't exist.
test.pop(1) # Returns the item at the given index and remove it. Throws IndexError when index is not in range.
del test[0] # No return value. Throws IndexError when index is not in range.
test.clear() # Empties the list
```

### Tuple
Immutable list.
### Set
TODO
### Dictionary
TODO

## Operators
- `/`: division (6 / 3 = 2.0 float)
- `**`: power (2 ** 3 = 8)
- `//`: floor division
- `%` modulus (5 % 2 = 1)
- round(number, digits)
  - `round(7.2355, 3) # 7.236`
  - `round(7.2345, 3). # 7.234, should be 7.235 ?`

## Scope
Block scope
- Local Scope: Variables in functions.
- Global Scope: Variables in modules. Yuo can read global variables in functions. But, use `global` when you need to modify it.

Note! It's still a global variable even though it is in a if statement.
```
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
test = 1

def increase_test():
    return test + 1     # Recommendation

test = increase_test()

def increase_enemies():
    global enemies      # Not recommendation. Modify global scope
    enemies +=1

def test():
    local_enemy = enemies[0]

if game_level < 5:
    global_enemy = enemies[0]

print(global_enemy)  # Works well.
print(local_enemy)   # No.
```


## OOP
- Use arguments (keyword and default value) to achieve multiple constructors.
