# List Comprehension

List Comprehension is a way to construct a new Python list from an iterable types: lists, tuples, and strings. All without using a for loop or the `.append()` list method.

In this project, you'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.

The project has two phases: first you'll use a for loop to implement the program. Then you'll learn how to use List Comprehension instead of a loop to achieve the same results.


[palabra](#palabra_clave)  
<span id="palabra_clave">**"palabra"**</span>


variable[.isupper()](#upper)  
variable[.lower()](#lower)  
variable[.append(valor)](#append)  
'element'[.join(valor)](#join)  
variable[.strip(valor)](#strip)  
[List comprehension](#list)  


#### Step 1:
In this project, you are going to build a program that takes a camelCase or PascalCase formatted string as input and converts that to a snake_case formatted string using two approaches. First, you'll use a for loop and then list comprehension to achieve the same results. You'll see how list comprehension can make your code more concise.

Start defining a new function named convert_to_snake_case() that accepts a string named pascal_or_camel_cased_string as input. For now, add a pass statement inside the function.

#### Step 2:
You need to add an empty list that will hold the characters of the string after you have converted them to snake case.

Inside the function, replace the pass statement by creating an empty list named snake_cased_char_list.

#### Step 3:
With the empty list in place, now you can start iterating through the input string and convert it into snake case.

Inside the function, below the list you just created, add a for loop to iterate through the pascal_or_camel_cased_string. Make sure to name the target variable char. For now, add a pass statement as a placeholder in the loop body.

#### Step 4:
In both camel case and pascal case, uppercase characters mark the beginning of new words. To convert the input string to snake case, you will need to check if the characters in the input string are uppercase.

You can use the <span id="upper">**".isupper()"**</span> string method to check if a character is uppercase. This method returns True if the character is uppercase and False if it is not.

Inside the for loop, add an if statement to check if the current character is uppercase. Move the pass statement inside the new if statement.

#### Step 5:
Inside the if statement body, you need to convert any uppercase character to lowercase and prepend an underscore to this lowercase character.

Use the <span id="lower">**".lower()"**</span> string method to convert uppercase characters to lowercase characters. Then, prepend an underscore to the character. Assign the results to a variable named converted_character.

#### Step 6:
Within the if statement body, you are going to add the converted character to the list you created earlier.

For this, the <span id="append">**".append()"**</span> method will be used. This method adds a given object to the end of the list it is invoked on.

Use the .append() method on the snake_cased_char_list to add the converted_character to the list.

#### Step 7:
You need to handle the characters that are already in lowercase by adding them to the list of converted characters.

Right after the if statement within the for loop, add an else clause and use the .append() method to add char to the snake_cased_char_list variable.

#### Step 8:
By this point, the variable snake_cased_char_list holds the list of converted characters. To combine these characters into a single string, you can utilize the <span id="join">**".join()"**</span>
 method.

The join method works by concatenating each element of a list into a string, separated by a designated string, known as the separator.

Example Code:
```python
result_string = ''.join(characters)
```

The example above joins together the elements of the characters list into a single string where each element is concatenated together using an empty string as the separator.

Now, right after the for loop, use the .join() method to join the elements in snake_cased_char_list using an empty string as the separator. Assign the result to a new variable named snake_cased_string.

#### Step 9:
In pascal case, strings begin with a capital letter. After converting all the characters to lowercase and adding an underscore to them, there's a chance of having an extra underscore at the start of your string.

The easiest way to fix this is by using the <span id="strip">**".strip()"**</span> string method, which removes from a string any leading or trailing characters among a set of characters passed as its argument. For example:

Example Code:
```python
original_string = "_example_string_"

clean_string = original_string.strip('_')
```  

The strip() method is applied to original_string. This removes any leading and trailing underscore. The result of the example above would be the string 'example_string'.

Declare a new variable named clean_snake_cased_string and assign it the result of the .strip() method applied to snake_cased_string , passing '_' as the argument to the method.

#### Step 10:
To wrap up the function, return the clean_snake_cased_string. This will complete the function and allow you to use it to convert strings from pascal or camel case to snake case.

Add a return statement at the end of the function to return the clean_snake_cased_string.

#### Step 11:
With the function complete, you can now use it inside another function.

Create a new function called main() with pass as the body of the function.

#### Step 12:
Inside the main() function, replace the pass statement, with a call to the convert_to_snake_case() function, passing the string 'aLongAndComplexString' as input.

To display the output, pass the function call as the argument to the print() function.

#### Step 13:
In order to display the output of the convert_to_snake_case() function, you need to call the main() function.

At the same level as the two existing functions, add a call to the main() function. You should see the given camel or pascal cased string converted to snake case upon execution.

#### Step 14 (List comprehension):
So far, in this project you have used a for loop to iterate over your input string and convert it into the desired output. Now you'll begin the transition from a for loop to a list comprehension.

Begin by commenting out all the lines of code inside the convert_to_snake_case() function. Don't delete them as they'll be helpful when you implement the logic using a list comprehension.

Remember to add the pass keyword to the function body to prevent the code from failing during the tests.

#### Step 15:
Replace the pass keyword with the variable snake_cased_char_list and assign it an empty list. Use the square brace notation to create the list.

#### Step 16:
You will need to convert uppercase characters to lowercase and add an underscore before them.

Before proceeding to work on the list comprehension, you're going to give your function a return value. In this way you'll be able to check the output.

Use the return statement to return the list snake_cased_char_list from your function.

#### Step 17:
Instead of returning the list snake_cased_char_list, you will need to join its elements into a single string using an empty string '' as the separator.

Modify the return statement to return the result of joining snake_cased_char_list with an empty string as a separator.

#### Step 18:
After joining the elements of the list snake_cased_char_list, you will need to remove any leading or trailing underscores from the resulting string. For this, use the strip method with the underscore character _ as an argument.

Method calls can be chained together, which means that the result of one method call can be used as the object for another method call.

Example Code:
```python
words_list = ['hello', 'world', 'this', 'is', 'chained', 'methods']
result = ' '.join(words_list).upper()
```  

In the example above, the .upper() method is chained to ' '.join(words_list), therefore .upper() is called on the result of the .join() call.

Modify the return statement by chaining to ''.join(snake_cased_char_list) a call to the .strip() method to remove any leading or trailing underscores.

#### Step 19:
In Python, a <span id="list">**"list comprehension"**</span> is a construct that allows you to generate a new list by applying an expression to each item in an existing iterable and optionally filtering items with a condition. Apart from being briefer, list comprehensions often run faster.

A basic list comprehension consists of an expression followed by a for clause:

Example Code:
```python
spam = [i * 2 for i in iterable]
```  

The above uses the variable i to iterate over iterable. Each elements of the resulting list is obtained by evaluating the expression i * 2 at the current iteration.

In this step, you need to fill the empty list snake_cased_char_list using the list comprehension syntax.

Turn your empty list into a list comprehension that converts each character in pascal_or_camel_cased_string into a lowercase character and prepends an underscore to it (the code you commented out before may help you write the expression). Use char to iterate over pascal_or_camel_cased_string.

#### Step 20: 
List comprehensions accept conditional statements, to evaluate the provided expression only if certain conditions are met:

Example Code
spam = [i * 2 for i in iterable if i > 0]
As you can see from the output, the list of characters generated from pascal_or_camel_cased_string has been joined. Since the expression inside the list comprehension is evaluated for each character, the result is a lowercase string with all the characters separated by an underscore.

Follow the example above to add an if clause to your list comprehension so that the expression is executed only if the character is uppercase.

#### Step 21:
Still, the final result is not exactly what you want to achieve. You need to execute a different expression for the characters filtered out by the if clause. You'll use an else clause for that:

Example Code:
```python
spam = [i * 2 if i > 0 else -1 for i in iterable]
```  

Note that, differently from the if clause, the if/else construct must be placed between the expression and the for keyword.

Modify your list comprehension so that when a character is not uppercase it remains unchanged.

#### Step 22:
Get rid of the commented lines of code inside the convert_to_snake_case() function to clean up the function definition.

#### Step 23:
Finally try out this new implementation by executing the program. Change the input string to 'IAmAPascalCasedString' and see if it comes out as 'i_am_a_pascal_cased_string', even though that's a lie.

If you've done everything correctly, you should see the input string converted into snake case, like before.

Congratulations! Now your convert_to_snake_case() function is ready.

---

<div align="center">
  <small>Practice material taken from: <a href="https://freecodecamp.org" target="_blank">freeCodeCamp.org</a></small>
</div>
<br>
<div align="center">
    <img src="https://img.shields.io/badge/freeCodeCamp-Python-FFD43B?style=for-the-badge&logo=freecodecamp&logoColor=white&labelColor=0A0A23&logoWidth=20" alt="freeCodeCamp + Python"
    alt="freeCodeCamp+Python"
    draggable="false" 
    style="pointer-events: none; user-select: none;">
</div>