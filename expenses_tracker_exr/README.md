# Lambda function

Lambda functions give you a concise way to write small, throwaway functions in your code.

In this project, you'll explore the power of Lambda Functions by creating an expense tracker. Your resulting app will demonstrate how you can use Lambda Functions for efficient, streamlined operations.

<br>

variable.[append(valor)](#append)  
lista.[insert(position, valor)](#insert)  
lista.[pop()](#pop)  
[lambda](#lambda) 
[map()](#map) 
[list()](#list)  
[sum()](#sum)  
[filter(item, list)](#filter)  
[palabra](#palabra_clave)  
[input()](#input)  

<br>

#### Step 1:
Before starting with the project, you are going to learn about lists.

Unlike numbers and strings, a list is a data type that works as a container for other values:

Example Code: 
```python
example_list = [1, 2, 3, 4]
empty_list = []
```

The list is characterized by the square brackets around all the values, and a comma between the values, like: ["A", "happy", "list"]. If the list does not contain any values, then it is an empty list: [].

A list can contain different data types: [1, "Up", ["Down", "Twice"]]. That includes all possible data types. It can also contain another list!

Create a variable called my_list and assign to it an empty list.

#### Step 2: 
To add items to a list, you can write them between the square brackets, separating the values with commas.

Add the numbers 1 and 2 inside the list.

#### Step 3:
Python has a handful of list methods. Such as methods for adding or removing list items.

You can add an item to the end of a list using the <span id="append">**"append()"**</span> method. For example:

Example Code: 
```python
example_list = [4, 5, 6]

example_list.append(7)
example_list now is [4, 5, 6, 7].
```  

Try to use the append() method to add 3 to my_list. Then print the list.

#### Step 4:
You can also access a single element to get its value.

Lists are zero-indexed like strings are. That means that the first element is at index 0, the second element is at index 1 and so on.

To access an element you use bracket notation. For example, example_list[1] is accessing the element at index 1, the second element, of example_list.

Print the first element of my_list.

#### Step 5: 
Python lists are mutable which means that the value of the list items can be changed. You can change the value of an element using the bracket notation.

Example Code: 
```python
example_list = [4, 5, 6, 7]
example_list[1] = 'oh'
```

This will make example_list have value of [4, 'oh', 6, 7].

Change the first element of my_list to 0, then print the list to check the value.


#### Step 6:
The <span id="insert">**"insert()"**</span> method can add an element at any position in a list. The first argument is the position at which the element has to be added, and the second argument is the element to add. For example, here's how to add a new element in the third position of example_list:

Example Code
example_list = [4, 5, 6, 7]

example_list.insert(2, 5.5)

print(example_list) # [4, 5, 5.5, 6, 7]
Using insert(), add 1 to my_list in the proper position so that it is counting upward, then print the list.

#### Step 7: 
The <span id="pop">**"pop()"**</span> method can be used to remove an element from a list. By default, it removes the last element of the list. You can pass an index as the argument to the method, and it will remove the element at the given index.

Example Code: 
```python
fruits_list = ["cherry", "lemon", "tomato", "apple", "orange"]

fruits_list.pop(2)

print(fruits_list) # ["cherry", "lemon", "apple", "orange"]
```

In this case, fruits_list.pop(2) removes the element at index 2 of the list.

Use pop() to remove the last element from my_list, then print my_list.


#### Step 8: 
Now that you have explored lists, remove all of the code you wrote for your review so you can begin the project.

#### Step 9: 
In this project, you're going to build a simple, yet functional expense tracker in Python.

Start by defining a function named add_expense that takes three parameters: expenses, amount and category. Use the pass keyword to fill the function body.

#### Step 10:
Create an empty list named expenses. You will use it to store each of your expenses.

#### Step 11: 
The expenses parameter of your add_expense function will be a list of expenses. You want to be able to add items at the end of your list. For that you'll use the .append() list method.

Add a call to the .append() method on the expenses list. Don't pass any arguments to .append() for now.

#### Step 12 (dictionary): 
A dictionary is another built-in data type in Python. A dictionary is a collection of data in the form of key-value pairs. Dictionaries are defined with curly braces ({}) and they contain key-value pairs separated by commas. Each key is followed by a colon (:) and the value:

Example Code:
```python
{'amount': 50.0, 'category': 'Food'}
```  

In the example above, 'amount' and 'category' are keys, and 50.0 and 'Food' are their corresponding values.

Create a dictionary with a key 'amount' and value of the amount parameter and pass your new dictionary to the .append() call.

#### Step 13: 
Add another key-value pair to the dictionary you are appending to the expense list. Use the string 'category' as the key, and the category parameter as the value.

Example Code:
```Python
expenses.append({'amount': amount, 'category': category})
```  

#### Step 14: 
Next, define a function named print_expenses that takes one parameter expenses. This function will later be used to display each expense in your list.

Fill the body of your new function with a pass statement.

#### Step 15: 
Inside the print_expenses function, create a for loop that iterates over each item in the expenses list. Use expense as the loop variable and move pass inside the loop body.

#### Step 16:
Next, you are going to display the details for each expense.

Inside the for loop, replace pass with a print() call and pass it the following f-string: f'Amount: {expense}, Category: {expense}'.

#### Step 17:
In Python, an important thing to know is that the same type of quote used to define a string cannot be used inside it. For example, the string 'I'm a string!' is not valid. To use the single quote inside that string you should either:

Escape the quote by prepending a backlash to it: 'I\'m a string!'
Or use double quotes to define the string: "I'm a string!" (preferred).
You can access values in a dictionary through its keys. You need to use bracket notation and include the key between the square brackets:

Example Code:
```python
my_dict = {'amount': 50.0, 'category': 'Food'}
my_dict['amount'] # 50.0
```

You are currently interpolating the expense dictionary in your f-string. Modify the f-string expression to access the value of the 'amount' key and the 'category' key in the expense dictionary.

#### Step 18:
You will need a function to calculate the total amount of expenses.

Define a function named total_expenses that takes one parameter expenses. Fill the function body with a pass statement for now.

#### Step 19: 
<span id="lambda">**"Lambda"**</span> functions are brief, anonymous functions in Python, ideal for simple, one-time tasks. They are defined by the lambda keyword, and they use the following syntax:

Example Code:
```python
lambda x: expr
```  

In the example above, x represents a parameter to be used in the expression expr, and it acts just like any parameter in a traditional function. expr is the expression that gets evaluated and returned when the lambda function is called.

Create a variable named test and assign it a lambda function that takes an x parameter and returns x * 2.

#### Step 20:
To call a lambda function you can use the usual function syntax with a pair of parentheses after the variable name.

Call your test lambda function and pass 3 as the argument. Then, print the result.

#### Step 21: 
Lambda functions can be valuably combined with the <span id="map">**"map()"**</span> function, which executes a specified function for each element in a collection of objects, such as a list:

Example Code: 
```python
map(lambda x: x * 2, [1, 2, 3])
```  

The function to execute is passed as the first argument, and the iterable is passed as the second argument.

The result of the example above would be [2, 4, 6], where each item in the list passed to map() has been doubled by the action of the lambda function.

Modify your print() call to print the result of calling map() with test as the first argument, and [2, 3, 5, 8] as the second argument. You won't be able to see a readable output yet.

#### Step 22:
You should see something like <map object at 0xd273a8> printed on the console, which is the string representation of the map object returned by map().

To obtain a readable output you need to turn the map object into a list. Do it by passing the map() call as the argument to the <span id="list">**"list()"**</span> function.

#### Step 23: 
The <span id="sum">**"sum()"**</span> function returns the sum of the items in the iterable which is passed as its argument. You are going to use sum() together with map() and lambda functions to get the total amount of expenses.

For now, make a little test and modify your current print() call replacing the list() call with a call to the sum() function passing it the current map() call as the argument.

#### Step 24:
Next, you are going to implement the same logic within the total_expenses function.

For now, delete both the test function and the print() call.

#### Step 25:
###### revisar...
In the total_expenses function, you'll now integrate a lambda function. Replace pass with a lambda function that has expense as its parameter.

expense is expected to be a dictionary, and your lambda function should return the value of the 'amount' key in the expense dictionary.

#### Step 26:
Now, call map() passing your lambda function as the first argument and the expenses list as the second argument.

#### Step 27:
Finally, pass your map() call to the sum() function to obtain the total expenses and return the result.

#### Step 28:
Next, define a function named filter_expenses_by_category that takes two parameters: expenses and category. Use pass to fill the function body.

#### Step 29:
Within the filter_expenses_by_category function, replace pass with a lambda function. Use expense as the parameter and evaluate the comparison between the value of the 'category' key of the expense dictionary and category using the equality operator.

#### Step 30:
The <span id="filter">**"filter()"**</span> function allows you to select items from an iterable, such as a list, based on the output of a function:

Example Code:
```python
filter(my_function, my_list)
```  

filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.

The result of the example above is an iterator containing the elements of my_list for which my_function returns True.

Within the filter_expenses_by_category function, call filter() passing the lambda function you wrote in the previous step as the first argument and the expenses list as the second argument.

#### Step 31:
Finally, return the result of the filter() call.

#### Step 32:
The next step is to define the main function, which will be the entry point of the interactive expense tracker program.

Define a function named main without parameters. Fill the function body with the expenses list you created at the beginning of this project. You will use this list to store the expense records.

#### Step 33:
A while loop is another kind of loop that runs a portion of code as long as a specified condition is True. The loop terminates when the condition becomes False:

Example Code
while condition:
```python
    <code>
```  

Below the expenses list, create a while loop. Use True for the condition, and print the string '\nExpense Tracker' inside the loop body to show the title of the program.

#### Step 34:
The while loop you created in the previous step is an infinite loop that will allow the program to continuously present menu options until the user decides to exit.

After the print() call, add another print() call to print the string '1. Add an expense'.

#### Step 35:
Next, add another print() call and pass the string '2. List all expenses'.

#### Step 36:
Provide the other menu options by printing the following three strings in your while loop: '3. Show total expenses', '4. Filter expenses by category', and '5. Exit'. Keep adding the print() calls in order.

#### Step 37:
The <span id="input">**"input()"**</span> function takes a user input and it returns the user input in the form of a string.

Inside your while loop, call the input() function passing the string 'Enter your choice: ' as the argument, and assign the result to a variable named choice.

#### Step 38:
You are going to use conditional statements to check the user's choice. If the choice is '1', it means the user wants to add an expense.

Still in the while loop, under the choice variable, write an if statement to check if choice equals the string '1'. If it's true, it will be the starting point for adding a new expense.

Inside the if statement body, declare a variable amount and assign it an empty input() call.

#### Step 39:
Inside the if statement, you should ask the user to enter the amount for the expense and store it in a variable.

Pass the string 'Enter amount: ' to your empty input() call, so you can store the expense.

#### Step 40:
The amount of the expense needs to be converted before performing any calculation. The float() function takes a string or an integer number as argument and returns a floating point number.

Pass input('Enter amount: ') to the float() function.

#### Step 41:
Inside your if statement, create a variable named category to store the expense category. Assign it a call to input() and use the 'Enter category: ' as the argument.

#### Step 42:
Once you have the expense details, you need to call the add_expense function to add the new expense to the expenses list.

After getting the amount and category using input(), call the add_expense function, passing three arguments: expenses, amount and category.

expenses is the empty list created in the main function earlier in this project.
amount is the amount of the expense.
category is the category of the expense.

#### Step 43:
To list all expenses, you can use an elif clause after an if statement. The elif checks additional conditions and only works following an if statement.

Create an elif clause to check if the user's choice equals the string '2'. Inside the elif clause, print the string '\nAll Expenses:'.

#### Step 44:
After the print() call, call the print_expenses function to display all the expenses that have been added so far. Pass the expenses list as the argument.

#### Step 45:
To show the total expenses, create an elif statement that checks if choice == '3'.

If it's true, it means the user wants to see the total expenses. So call print() and pass the string '\nTotal Expenses: ' as the first argument and total_expenses(expenses) as the second argument.

#### Step 46:
Create another elif clause that checks if choice == '4'. Inside the new elif, create a variable category and assign it input('Enter category to filter: ') to filter the expense category.

#### Step 47:
After getting the category, print the following f-string f'\nExpenses for {category}:'.

#### Step 48:
After your print() call, you need to filter the expenses and print the filtered list. Declare a variable expenses_from_category and assign it a call to filter_expenses_by_category passing expenses and category as the argument.

#### Step 49:
Still within the elif clause, pass the expenses_from_category iterator to a print_expenses call.

#### Step 50:
To provide a way to exit the program, use another elif clause to check if choice equals the string '5'.

Inside the new elif clause, print the string 'Exiting the program.' to show that the program is terminating its execution.

#### Step 51:
Finally, to stop the execution of the while loop, add the break statement inside your last elif clause.

#### Step 52:
Finally, call your main() function, and try the expense tracker program in the console.

With that, the expense tracker project is complete!

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