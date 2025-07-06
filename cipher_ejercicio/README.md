# Learn String Manipulation by Building a Cipher

In this proyect, you'll learn fundamental programming concepts in Python, such as variables, functions, loops, and conditional statements. You'll use these to code your first programs.  

<br>

## Methods and functions used in this proyect

[Print()](#print)  
[Len()](#len)  
[Type()](#type)  
[for loop](#for)  


### Funtions that I learned:

variable_name.[find](#find)(key_name)  
variable_name.[lower](#lower)()  
variable_name.[index](#index)(key_name)  
variable_name.[isalpha](#isalpha)()

<br>

## Variables: 

A variable is a name that references or points to an object. You can declare a variable by writing the variable name on the left side of the assignment operator = and specifying the value to assign to that variable on the right side of the assignment operator:

**Example Code:**    
```Python
variable_name = value  
```   


Variables can store values of different data types. You just assigned an integer value, but if you want to represent some text, you need to assign a string. Strings are sequences of characters enclosed by single or double quotes, but you cannot start a string with a single quote and end it with a double quote or vice versa:

Example Code:  
```python  
string_1 = "I am a string"
string_2 = 'I am also a string'
string_3 = 'This is not valid"  
```

You can use the built-in function <span id="print">**"Print()"**</span> to print the output of your code on the terminal.

Functions are reusable code blocks that you can call, or invoke, to run their code when you need them. To call a function, you just need to write a pair of parentheses next to its name. You will learn more about functions very soon.

An argument is an object or an expression passed to a function — added between the opening and closing parentheses — when it is called:

```python  
greet = 'Hello!'
print(greet)
```

The code in the example above would print the string 'Hello!', which is the value of the variable greet passed to print() as the argument.

Each string character can be referenced by a numerical index. The index count starts at zero. So the first character of a string has an index of 0. For example, in the string 'Hello World', 'H' is at index 0, 'e' is at index 1, and so on.

Each character of a string can be accessed by using bracket notation. You need to write the variable name followed by square brackets and add the index of the character between the brackets:  

Example Code:   

```python  
text = 'Hello World'
r = text[8]
``` 

You can also access string characters starting from the end of the string. The last character has an index of -1, the second to last -2 and so on.

```python
text = 'Hello World'
print(text[-1])
```

You can access the number of characters in a string with the built-in <span id="len">**"Len()"**</span> function.

Another useful built-in function is <span id="type">**"Type()"**</span>, which returns the data type of a variable.

#### Key aspects of variable naming in Python are:

Some words are reserved keywords (e.g. for, while, True). They have a special meaning in Python, so you cannot use them for variable names.
Variable names cannot start with a number, and they can only contain alpha-numeric characters or underscores.
Variable names are case sensitive, i.e. my_var is different from my_Var and MY_VAR.
Finally, it is a common convention to write variable names using snake_case, where each space is replaced by an underscore character and the words are written in lowercase letters.

## Methods:

We are going to use the <span id="find">**"find()"**</span> method to find the position in the alphabet of each letter in your message. A method is similar to a function, but it belongs to an object.

Example Code:
```python
sentence = 'My brain hurts!'
sentence.find('r')
```

Above, the .find() method is called on sentence (the string to search in), and 'r' (the character to locate) is passed as the argument. The sentence.find('r') call will return 4, which is the index of the first occurrence of 'r' in sentence.



## Exercise

#### Step 14:  
The first kind of cipher you are going to build is called a Caesar cipher. Specifically, you will take each letter in your message, find its position in the alphabet, take the letter located after 3 positions in the alphabet, and replace the original letter with the new letter.

To implement this, you will use the .find() method discussed in the previous step. Modify your existing .find() call passing it text[0] as the argument instead of 'z'.

#### Step 15:  
The print() function gives you only an output in the console, but functions and methods can have a return value that you can use in your code.

Now assign alphabet.find(text[0]) to a variable named index. In this way, index will store the value returned by alphabet.find(text[0]).

#### Step 16:  
Next, print the index variable to the console.

#### Step 17:  
.find() returns the index of the matching character inside the string. If the character is not found, it returns -1. As you can see, the first character in text, uppercase 'H', is not found, since alphabet contains only lowercase letters.

You can transform a string into its lowercase equivalent with the .lower() method. Add another print() call to print text.lower() and see the output.

#### Step 18:  
Remove the last print() call. Then, instead of text[0], pass text[0].lower() as the argument to your .find() call and see the output.

#### Step 19:  
Declare a new variable named shifted. Use the bracket notation to access the value of alphabet at index index and assign it to your new variable.

#### Step 20:  
Print your shifted variable.

#### Step 21:
As you can see from the output, 'h' is at index 7 in the alphabet string. Now you need to find the letter at index 7 plus the value of shift. For that, you can use the addition operator, +, in the same way you would use it for a mathematical addition.

Modify your shifted variable so that it stores the value of alphabet at index index + shift.

#### Step 22:  
Repeating the process of locating the letter inside the alphabet and determine the shifted letter for each character in text can be tedious. Thankfully, you can simplify it using a loop.

For now, remove all the lines of code below the declaration of the alphabet variable.

#### Step 23 (<span id="for">**for loop**</span>):  
A loop allows you to systematically go through a sequence of elements and execute actions on each one.

In this case, you'll employ a for loop. Here's how you can iterate over text:

Example Code:  
```python
for i in text:
```  

for is the keyword denoting the loop type. i is a variable that sequentially takes the value of the elements in text. The statement ends with a colon, :.

Below the line where you declared alphabet, write a for loop to iterate over text. Use i as the loop variable.

Doing so, there is an error in the terminal. You will learn about it in the next step.

#### Step 24(indentation):  
The code to execute at each iteration — placed after the : — constitutes the body of the loop. This code must be indented. In Python, it is recommended to use 4 spaces per indentation level. This indented level is a code block.

Example Code:  
```python
for i in text:
    print(i)
``` 

Python relies on indentation to indicate blocks of code. A colon at the end of a line is a signal that a new indented block of code will follow.

So, when no indented block is found after the final colon, the code execution stops and an IndentationError is thrown. This code will not show the output and instead raise an IndentationError:

Example Code:  
```python 
for i in text:
print(i)
```  

Give your for loop a body by adding a call to print(i). Remember to indent the loop body.

#### Step 25:  
The iteration variable can have any valid name, but it's convenient to give it a meaningful name.

Rename your i variable to char.

#### Step 26:  
Inside the for loop, before printing the current character, declare a variable called index and assign the value returned by alphabet.find(char) to this variable.

#### Step 27:  
Currently, the print() function is taking a single argument char, but it can take multiple arguments, separated by a comma.

Add a second argument to print(char) so that it prints the character and its index inside the alphabet.

#### Step 28:  
find is again returning -1 for uppercase letters, and for the space character, too. You are going to take care of the space later on.

For now, instead of iterating over text, change the for loop to iterate over text.<span id="lower">**lower()**</span>.

#### Step 29:  
At the end of your loop body, declare a variable called new_index and assign the value of index + shift to this variable.

#### Step 30:  
Strings are immutable, which means they cannot be changed once created. For example, you might think that the following code changes the value of my_string into the string 'train', but this is not valid:

Example Code:
```python
my_string = 'brain'
my_string[0] = 't'
```  

Confirm that by using the bracket notation to access the first letter in text and try to change it into a character of your choice. You will see the ouput disappear and an error appear.

#### Step 31:  
When you try to change the individual characters of a string as you did in the previous step, you get a TypeError, which occurs when an object of inappropriate type is used in your code.

As you can see from the error message, strings do not support item assignment, because they are immutable. However, a variable can be reassigned another string:

Example Code:  
```python
message = 'Hello World'
message = 'Hello there!'
```  

Delete the text[0] line and reassign text the string 'Albatross'.

#### Step 32:  
As you can see, each character of the reassigned string gets printed inside the loop.

Go back to the original string by deleting the text reassignment.

#### Step 33:  
Now you need to create a new_char variable at the end of your loop body. Set its value to alphabet[new_index].

#### Step 34:  
Next, print new_char and see the output.

#### Step 35:  
Clean the output a bit. Delete print(char, index), and turn the last print() call into print('char:', char, 'new char:', new_char).

#### Step 36:  
At the moment, the encrypted character is updated in every iteration. It would be better to store the encrypted string in a new variable. Before your for loop, declare a variable called encrypted_text and assign an empty string ('') to this variable.

#### Step 37:   
Now, replace new_char with encrypted_text. Also, modify the print() call into print('char:', char, 'encrypted text:', encrypted_text) to reflect this change.

#### Step 38:  
Instead of assigning alphabet[new_index] to encrypted_text, assign the current value of encrypted_text plus alphabet[new_index] to this variable.

#### Step 39:  
You can obtain the same effect of a = a + b by using the addition assignment operator:

Example Code: 
```python
a += b
```  

The addition assignment operator enables you to add a value to a variable and then assign the result to that variable.

Use the += operator to add a value and assign it at the same time to encrypted_text.

#### Step 40 (comparison operators):  
Comparison operators allow you to compare two objects based on their values. You can use a comparison operator by placing it between the objects you want to compare. They return a Boolean value — namely True or False — depending on the truthfulness of the expression.

Python has the following comparison operators:

| Operator |	Meaning |
| -------- | ------ |
| == | Equal |
| !=	 | Not equal |
| >	| Greater than |
| <	| Less than |
| >=	 | Greater than or equal to |
| <=	| Less than or equal to |

At the beginning of your loop body, print the result of comparing char with a space (' '). Use the equality operator == for that.

#### Step 41 (conditionals):  
Currently, spaces get encrypted as 'c'. To maintain the original spacing in the plain message, you'll require a conditional if statement. This is composed of the if keyword, a condition, and a colon :.

Example Code: 
```python 
if x != 0:
    print(x)
```  

In the example above, the condition of the if statement is x != 0. The code print(x), inside the if statement body, runs only when the condition evaluates to True (in this example, meaning that x is different from zero).

At the top of your for loop, replace print(char == ' ') with an if statement. The condition of this if statement should evaluate to True if char is an empty space and False otherwise. Inside the if body, print the string 'space!'. Remember to indent this line.

#### Step 42:  
Now, instead of printing 'space!', use the addition assignment operator to add the space (currently stored in char) to the current value of encrypted_text.

#### Step 43:  
A conditional statement can also have an else clause. This clause can be added to the end of an if statement to execute alternative code if the condition of the if statement is false:

Example Code: 
```python
if x != 0:
    print(x)
else:
    print('x = 0')
```  

As you can see in your output, when the loop iterations reach the space, a space is added to the encrypted string. Then the code outside the if block executes and a c is added to the encrypted string.

To fix it, add an else clause after encrypted_text += char and indent all the subsequent lines of code except the print() call.

#### Step 44:  
Try to assign the string 'Hello Zaira' to your text variable and see what happens in the terminal.

You'll see a string index out of range exception. Don't worry, you'll figure out how to fix it soon!

#### Step 45:  
When the loop reaches the letter Z, the sum index + shift exceeds the last index of the string alphabet. Therefore, alphabet[new_index] is trying to use an invalid index, which causes an IndexError to be thrown.

You can notice that the output in the terminal stops at the space immediately before the Z, the last print before the error is thrown.

In this case, the modulo operator (%) can be used to return the remainder of the division between two numbers. For example: 5 % 2 is equal to 1, because 5 divided by 2 has a quotient of 2 and a remainder of 1.

Surround index + shift with parentheses, and modulo the expression with 26, which is the alphabet length.

#### Step 46:
If you wish to incorporate additional characters into the alphabet string, such as digits or special characters, you'll find it's necessary to manually modify the right operand of the modulo operation.

Replace 26 with len(alphabet) to avoid this issue.

#### Step 47: 
Next, modify your print() call to print 'encrypted text:', encrypted_text and put it outside the for loop, so that the encrypted string is printed one time.

#### Step 48:  
Right before the print call, add another one and pass 'plain text:', text as the arguments to print(). Use the same indentation.

#### Step 49 (function):  
A function is essentially a reusable block of code. You have already met some built-in functions, like print(), find() and len(). But you can also define custom functions like this:

Example Code: 
```python
def function_name():
    <code>
```  

A function declaration starts with the def keyword followed by the function name — a valid variable name — and a pair of parentheses. The declaration ends with a colon.

Right after your shift variable, declare a function called caesar and indent all the following lines to give your new function a body.

#### Step 50: 
In Python, the scope of a variable determines where that variable can be accessed:

Variables defined outside a function have a global scope and they can be accessed from any part of your code.

Variables defined inside a function are local to that function and cannot be accessed outside of it.

To see this in action, try to print the alphabet variable at the end of your code. This will raise a NameError exception.

You should see an error message indicating that alphabet is not defined. This is because alphabet is defined inside the caesar function and is not accessible outside of it.

#### Step 51:  
Now, fix the error by removing the line that tries to print the alphabet variable outside of the caesar function.

#### Step 52:  
To execute, a function needs to be called (or invoked) by appending a pair of parentheses after its name, like this:

Example Code: 
```python
function_name()
```  

At the end of your code, call your caesar function. Pay attention to the indentation.

#### Step 53 (Parameters): 
Now you should see the output again. Although this approach works, it doesn't significantly enhance the code's reusability. Repeatedly calling your function will result in the same outcome. However, functions can be declared with parameters to introduce versatility and customization:

Example Code: 
```python
def function_name(param_1, param_2):
    <code>
```

Parameters are variables that you can use inside your function. A function can be declared with different number of parameters. In the example above, param_1 and param_2 are parameters.

Modify your function declaration so that it takes two parameters called message and offset.

After that, you'll see an error appear in the terminal. You'll see how to solve it in the next steps.

#### Step 54:  
Inside your function body, rename the text and shift variables to message and offset, respectively.

#### Step 55: 
Currently, your code raises a TypeError, because the caesar function is defined with two parameters (message and offset), therefore it expects to be called with two arguments.

Calling caesar() without the required arguments stops the execution of the code.

Give message and offset values, by passing text and shift as arguments to the caesar function call.

#### Step 56: 
At the bottom of your code, after your existing caesar(text, shift) call, call your function again.

This time, pass the text variable and the integer 13 as arguments.

#### Step 57:  
Currently, every single letter is always encrypted with the same letter, depending on the specified offset. What if the offset were different for each letter? That would be much more difficult to decrypt. This algorithm is referred to as the Vigenère cipher, where the offset for each letter is determined by another text, called the key.

Start transforming your Caesar cipher into a Vigenère cipher by removing the two function calls.

#### Step 58 (Vigenère cipher algorithm):  
Now modify your function declaration: change the function name into vigenere and the second parameter into key.

#### Step 59:  
Delete your shift variable. Then, declare a new variable called custom_key and assign the value of the string 'python' to this variable.

#### Step 60:  
Since your key is shorter than the text that you will have to encrypt, you will need to repeat it to generate the whole encrypted text. At the beginning of your function body, declare a key_index variable and set it to zero.

#### Step 61 (comments):  
When coding, readability is key. Comments serve as effective notes, explaining the logic behind your code. They prove valuable when returning to a project after some time and also aid your colleagues in understanding the code.

In Python, you can write a comment using a #. Anything that comes after the # won't be executed.

Before your if statement, add a comment saying Append space to the message.

#### Step 62: 
Next, inside the else block, declare a variable called key_char and assign it the value of key at the index key_index mod(%) the length of key.

#### Step 63:  
You will need to increase the key_index count for the next iteration. To do this, after the line you just added and in the same code block, use the addition assignment operator to increment key_index by one.

#### Step 64: 
Inside the else clause, write a comment saying Find the right key character to encode.

#### Step 65: 
The <span id="index">**"index()"**</span> method is identical to the .find() method but it throws a ValueError exception if it is unable to find the substring.

A ValueError is a built-in exception that is raised when an argument with the right type but inappropriate value is passed to a function.

After incrementing key_index, declare a variable named offset. Find the index that key_char has in alphabet and assign it to offset. Use the .index() to find the index.

#### Step 66:  
Above the offset variable, create another comment saying Define the offset and the encrypted letter.

#### Step 67 (Return): 
At the moment, your function prints some strings, but these values cannot be used by other parts of code to perform any actions.

For that purpose, you need to use a return statement:

Example Code:
```python
def foo():
    return 'spam'
```  

You need to write return followed by a space and the value that the function should return. Once the return statement is found, that value is returned and the execution of the function stops, proceeding to the next line of code after the function call. In the example above, the foo function returns the string 'spam'.

Remove the two print() calls from your function and return encrypted_text.

#### Step 68: 
Call your function passing text and custom_key as the arguments. Store the return value of the function call in a variable called encryption.

#### Step 69: 
And now, try to print encryption to see the actual output on the terminal.

**Code so far:**
```python
text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:        
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text
    
encryption = vigenere(text, custom_key)
print(encryption)
```  


#### Step 70: 
Encryption and decryption are opposite processes and your function can do both with a couple of tweaks.

Add a third parameter called direction to your function definition. Also, comment out the last two lines of code to avoid errors in the console.

#### Step 71: 
All you need to do is multiply the offset by the direction in the new_index assignment. The multiplication operator in Python is *.

#### Step 73: 
Check if the function can decrypt the string back to the plain text.

Declare another variable called decryption and assign it vigenere(encryption, custom_key, -1).

#### Step 74:
Now print your decryption variable.

```python
encryption = vigenere(text, custom_key, 1)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)
```  

#### Step 75: 
Now, your function can be used both to encrypt and decrypt a message. Clean up your code with better variable names.

Change each occurrence of encrypted_text into final_message.

#### Step 76: 
Update your comments too. Your second comment should say encode/decode in place of encode. Your third comment should say encrypted/decrypted in place of encrypted.

#### Step 77 (default arguments): 
Functions can be called with default arguments. A default argument indicates the value that the function should take if the argument is not passed. For example, the function below accepts three arguments but you can call it passing two arguments. The third one will assume the specified value by default:

Example Code: 
```python
def foo(a, b, c=value):
    <code>
```

Modify the vigenere function so that its direction parameter has a default value of 1.

#### Step 78: 
Now you can remove the third argument from your first function call.

encryption = vigenere(text, custom_key)
print(encryption)
decryption = vigenere(encryption, custom_key)
print(decryption)

#### Step 79: 
Right now, punctuation, special characters or digits are not encoded/decoded correctly.

Check this by adding an exclamation mark at the end of the text string.

#### Step 80:  
The <span id="isalpha">**"isalpha()"**</span> method returns True if all of the characters of the string on which it is called are letters. For example, the code below returns True:

Example Code: 
```python
'freeCodeCamp'.isalpha()
# True
```  

Delete the condition char == ' ' and replace it by calling the .isalpha() method on char.

#### Step 81 (not): 
The not operator is used to negate an expression. When placed before a truthy value — a value that evaluates to True — it returns False and vice versa.

Add the not operator at the beginning of the if condition to check if the character is not alphabetic.

#### Step 82: 
Modify your comment into Append any non-letter character to the message.

#### Step 83: 
The pass keyword can be used as a placeholder for future code. It does not have any effect in your code but it can save you from errors you would get in case of incomplete code:

Example Code: 
```python
def foo():
    pass
```

Calling vigenere with 1 to encrypt and -1 to decrypt is fine but it might be a little bit cryptic. Create a new function called encrypt that takes message and key parameters, and use pass to fill the function body.

#### Step 84: 
Delete the pass keyword, and return vigenere(message, key) from your new function.

#### Step 85: 
Define another function named decrypt with the same parameters as encrypt. This time return vigenere(message, key, -1).

#### Step 86: 
Next, modify your encryption and decryption variables by calling encrypt and decrypt, respectively, in place of vigenere.

```python
def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)
```  

#### Step 87:  
It works! Now, you are going to start with an encrypted message to be decrypted.

Change the value of text to the string 'mrttaqrhknsw ih puggrur'.

#### Step 88:  
Since this time you are starting from an encrypted string to decrypt, you won't need the encryption variable anymore.

Delete encryption and the print(encryption) call. Also, comment out the last two lines of your code.

#### Step 89: 
Two or more strings can be concatenated by using the + operator. For example: 'Hello' + ' there!' results in 'Hello there!'.

Call the print() function and use the + operator to concatenate the text variable to the string 'Encrypted text: '. Pay attention to the spacing.

#### Step 90: 
Below the print() call you just added, add another print() call to print Key: python by concatenating the string 'Key: ' and the value of the custom_key variable.

#### Step 91 (f-strings):  
In Python, there's a way to easily format strings. f-strings enable you to interpolate values in your strings.

Interpolation means writing placeholders that will be replaced by the specified values when the program runs. For example, you can get the same result of 'Encrypted text: ' + text with f'Encrypted text: {text}'. You need to put an f before the quotes to create the f-string and write the variables or expressions you want to interpolate between curly braces.

Modify the first print() call to use an f-string.

#### Step 92:  
Next, modify print('Key: ' + custom_key) to use an f-string.

#### Step 93:  
The newline character \n is a special sequence used to represent a new line. You can write a backslash \ followed by an n as a normal sequence of characters in a string and it will be replaced by a new line in the output when the program runs.

Put a newline character at the beginning of your first print call and see the output.

#### Step 94: 
Uncomment the decryption variable and change its value by passing text as the first argument to decrypt.

#### Step 95:  
Uncomment your last print() call and change it to use the f-string f'\nDecrypted text: {decryption}\n' as the argument.

#### Step 96:  
Wait a minute! You cannot decrypt anything with the wrong key. Try with 'happycoding'.

With that, your cipher project is complete.


<div align="center">
  <small>Practice material taken from: <a href="https://freecodecamp.org" target="_blank">freeCodeCamp.org</a></small>
</div>
<br>
<div align="center">
    <img src="https://img.shields.io/badge/freeCodeCamp-Python-FFD43B?style=for-the-badge&logo=freecodecamp&logoColor=white&labelColor=0A0A23&logoWidth=20" alt="freeCodeCamp + Python">
</div>
