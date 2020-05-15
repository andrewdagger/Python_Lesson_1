
## Strings

Text data is called a String in Python

"This is a String"

len() shows the length of the string

To create or print strings with multiple lines, you can add the \n to the part of the string you would like to separate, or you can use three of the same quotation marks before and after the string you would like to create. 

"This is how you have extra \"extra strings\" in Python"
'This is how you have extra "extra strings" in Python'

print("This string\nwill be separated\ninto three lines!!!") 

or 

print("""Dear student,

We are super excited to have you in this course.

Sincerely,
The Coder Team
""")


## Brackets and Slicing 

slicing [0:20] or [20:] counts the length of the string and displays those characters (counting from 0)
Note that Python starts counting indeces from 0, hence, the letter 'a' above is at index 5 but it is the sixth element of that string.
"What a beautiful day to learn how to program"[5]

"W" --> 0
"h" --> 1
"a" --> 2
"t" --> 3
" " --> 4
"a" --> 5

"What a beautiful day to learn how to program"[0:20]
'What a beautiful day'

"What a beautiful day to learn how to program"[24:]
'learn how to program'

"What a beautiful day to learn how to program"[10:20]
tiful day 


## Intergers 

Intergers are whole numbers. 

use str() to convert data types to strings i.e str(390)
use int() to convert data types to integers i.e int(23)
use float() to convert data types to floats i.e float(5)

## Floating point numbers

Floating-point numbers are numbers with decimals. No decimals and a dot at the end of a number will still evaluate to a float.

Floating numbers will be rounded down when converted to integers

## Booleans

Booleans are data types represented most commonly as True or False evaluations of a statement or several. When we compare numbers or strings with one another, or when we try to find whether a given element is part of a list or dictionary, we are essentially creating booleans.

A boolean data type is also treated as a number. Statements that evaluate to True are also equal to the number 1. In contrast, elements or statements that evaluate to False, are also treated as 0.

Here is a list of the most commonly used boolean comparison evaluators.

Symbol	Functionality
==	exactly equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to
!= not equal to

False is 0, True is 1

and will evaluate True as long as both statements are True 
or will evaluate to True as long as there is one statement that is True. If both statements are false, or will always print out False.

## Lists
Lists in Python are some of the most versatile data structures available. They can hold multiple data types at the same time, and they can all be accessed using the same conventions (we will see these later on in the lesson). We usually want to have only one data type per list, but it is important to know that more are allowed as well.

To create a list you have to use square brackets [ ] and separate the values in them with commas ,. Let's take a look at several examples with a single data type in each, and several in some.

[1, 'Ray', True, 3.7]

[['Friend', 'Age', 'Town'],
['Andrew', 29, 'Kansas City'],
['Hanna', 30, 'Denver'],
['Kristen', 27, 'New Haven']]

When you have indices inside indexs, you can grab them with sub-indexs. For example, [1, 'Ray', True, 3.7][1][1] will return 'a' but [1, 'Ray', True, 3.7][1]will return 'Ray'. Strings indexes and integers so as well, this will not work for booleans. For example, [[1, 2, 3], [4, 5, 6], [7, 8, 9]][0][1] will return '2' because Python counts from 0. [[1, 2, 3], [4, 5, 6], [7, 8, 9]][0][0] will return '1'

## Dictionaries
Dictionaries are analogous data structures to what is called a JSON file. These dictionaries are esentially key-value pairs of data where the key is the variable name (and can be a string or a number), and the value is any kind of data type (e.g. a list, another dictionary, numbers, strings, booleans, etc.).

You can initialize a dictionary in several ways:

You can create a dictionary using brackets var = {"key": value(s)}

You can create a dictionary dict(key = value, key2 = value2

## Tuples
Tuple are lists cousins except that they are immutable. This means that the content of a tuple cannot be altered. What you can do instead is to take the elements in a tupe and unpack them into another data structure, i.e. a list. 

Tuples are usually denoted with parentheses (). They can be created without parentheses but a tuple with a single item needs to have a comma after the number otherwise python whill display it under what its data type.

To unpack elements in a tuple we need to assign such elements to new variables, create a copy of the tuple and change its data structure.

## Variables
You want to think of variables as buckets. These buckets can hold anything you need them to hold in Python but they do have some naming conventions we need to be aware of. Let's look at some variables first and visit the naming conventions afterwards.

Variables can be changed 

variable4 = [1, 2, 3, 4, 5]
print(variable4); type(variable4)

variable4[0] = 20
print(variable4)

Python memory doesn't hold the operation, but it does hold the result of the operation. This is the variable

A Variable can only contain letters, underscores and numbers. Variables cannot be only numbers.

## Sets
To get a set started, all you need is to create a data structure with a set of brackets {}, just like a dictionary, or call the function set() on a list.

A dictionary has to have a key, a column and a value. Sets are just lists. Sets are unordered and don't support duplicates.

Sets, like lists, tuples, and dictionaries, have methods to add or remove elements from them. Keep in mind though that no matter how many times you try to add an element that already exists in the set, the set will always evaluate only one of the duplicated elements. For example, let's use the method .add() on out set a_set to add the letter 'a' again.

To remove an element you can use the method .remove() on the set and pass in that element you wish to remove as the argument of the method. Please note that if you try to remove an element that does not exist in the set, python will give you back an error.

## Printing

Most common message in Python

f in the string allows for formatted printing: 

my_age = 31
print(f"I am {my_age} years old!")

You can also add {var} and .format (var="formatted:)) 

print("Hi! This is a {var} printing job!".format(var="formatted"))

For example, a %s inside a string and a % outside of one will point to the nearest object of that data type NOTE: s is for string, i is for integer and f is for float

my_age = 27
print("Hi, Everyone! My name is Ramon and I am %i young! :)" % my_age)

day = "Saturday"
month = "May"

print("This course began on the first %s of the month of %s, 2020." % (day, month))
# don't forget to wrap the arguments after the % sign in parenthesis

num1 = 1
num2 = 3

print("Have you tried to divide %i by %i and mulply the result, %f, back?" % (num1, num2, num1 / num2))

## Maths


Operator	What this does!
+	Addition
-	Subtraction
*	Multiplication
**	Exponentiation
/	Division
%	Modulo or remainder
//	Floor division

Operator	What this does!
+=	Add and assign
-=	Subtraction and assign
*=	Multiplication and assign
**=	Exponentiation and assign
/=	Division and assign
%=	Modulo or remainder and assign
//=	Floor division and assign - displays the lower number when the result is not evenly divided

Pemdas
parenthesis, exponents, multiplication, division, addition, subtraction

You can also multiple and add strings.

## Packages
A package is code that is already written that can be imported. 

To figure out which functions are exist in a given package you can call the dir() function on the package once you load it into your environment.

import math # load package
dir(math)

## Lists, Arrays and Matrices
`Arrays` in computer science and data analytics are collections (or `lists`) of elements that have an indext attached to them. Think of any of the spreadsheet tools you have used in the past, most of them probably had rows and columns (which are each arrays), and the combination of both, a cell or element, came with a row number (the indect), and a column letter (the name of the array). 

In Python, lists are our first representation of arrays and nested lists are our first representation of a `matrix` (e.g. the entire spreasheet).


$  pip install

## Short cut

a to add a cell above

b to add a cell below

dd to delete

