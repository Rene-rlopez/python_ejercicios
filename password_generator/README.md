# Learn regular expressions by building a password generator

## import

1. **re:** 
	A regular expression, or regex, is a pattern used to match a specific combination of characters inside a string. It is a valid alternative to if/else conditional statements when you need to match or find patterns inside a string for validation purposes, character replacement, and others.  
	
	- **compile()**: The compile() function from the re module compiles the string passed as the argument into a regular expression object that can be used by other re methods.
	- **search()**: The search() function from the re module analyzes the string passed as the argument looking for the first place where the regex pattern matches the string.
	- **findall()**: It's similar to search but it returns a list with all the occurrences of the matched pattern.
	- **Character class**: is indicated by square brackets and matches one character among those specified between the brackets. For example, ma[dnt] matches either mad, man, or mat.
	- **all()**: is a built-in Python function that returns True if all the elements inside a given iterable evaluate to True. Otherwise, it returns False.
	- **Generator expressions**: A Generator expressions follow the syntax of list comprehensions but they use parentheses instead of square brackets. Memory can be saved by using a generator expression.
2. **secrets:** Generador seguro de números aleatorios.
3. **string:** Provee conjuntos como ascii_letters, digits y punctuation.


## Raw string
Python provides a particular type of string called raw string. Raw strings are prefixed with a r. The key distinction from regular strings lies in how they handle the backslash character: in raw strings, backslashes are treated as literal characters rather than escape characters. When writing regular expressions, using raw strings is a good practice, since they can usually contain a lot of \ characters.   


### USAGE EXAMPLES: 

### String:
```python
cadena = 'Hello\nWorld'
print(cadena)
```

### Salida:
```python
Hello
World
```

### Raw string:
```python
cadena = r'Hello\nWorld'
print(cadena)
```

### Salida:
```python
Hello\nWorld
```   

---

### Regular expressions with the re module:  

Using raw strings makes the pattern more readable and shorter.  

```python
import re
re.search(r"\d+", "I have 123 cats")
```  

> \d means "a digit", and if you don't use r"", you have to write it like this: "\\d+".  
In the same way the [0-9] class is equivalent to \d, the [^0-9] class is equivalent to \D. Alphanumeric characters can be matched with \w and non-alphanumeric characters can be matched with \W.  


---

### File paths in Windows:

```python
path = r"C:\nueva\carpeta\archivo.txt"
```  
> Without r, Python would interpret \n as a newline.  


## 📌 Practical Rule  

Use r"" whenever:

- You are writing regular expression patterns.

- You are writing file paths in Windows.

- You want backslashes (\) not to be interpreted as special characters.


Quick Example with Regex

```python
import re

# with raw string
re.search(r"\w+\d+", "abc123")  # works

# without raw string (harder to read)
re.search("\\w+\\d+", "abc123")  # also works, but it's ugly
```  
