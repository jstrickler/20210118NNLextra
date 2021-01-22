# Chapter 4 Array Types


## Objectives

* Using single and multidimensional lists and tuples
* Indexing and slicing sequential types
* Looping over sequences
* Tracking indices with enumerate()
* Using range() to get numeric lists
* Transforming lists
<div style="page-break-after: always"></div>

## About Array Types
* Array types
  ** str
  ** bytes
  ** list
  ** tuple
* Common properties of array types
  ** Same syntax for indexing/slicing
  ** Share some common methods and functions
  ** All can be iterated over with a  for loop

Python provides many data types for working with multiple values. Some of these are array types. These hold values in a sequence, such that they can be retrieved by a numerical index.

A str is an array of characters. 
A bytes object is array of bytes. 

All array types may be indexed in the same way, retrieving a single item or a slice (multiple values) of the sequence.

Array types have some features in common with other container types, such as dictionaries and sets. These other container types will be covered in a later chapter. 

All array types support iteration over their elements with a for loop.

```{admonition} TIP
All arrays are iterable
```

<div style="page-break-after: always"></div>


### typical_arrays.py

fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']
name = "Eric Idle"
knight = 'King', 'Arthur', 'Britain'

print(fruits[3])  # <1>
print(name[2])  # <2>
print(knight[1])  # <3>


<div style="page-break-after: always"></div>
## Lists
****
* Array of objects
* Create with [  ]
* Add items with append(), extend(), or insert
* Remove items with del, pop(), or remove()
****

A list is one of the fundamental Python data types. Lists are used to store multiple values. The values may be similar – all numbers, all user names, and so forth; they may also be completely different. Due to the dynamic nature of Python, a list may hold values of any  type, including other lists.

Create a list with a pair of square brackets. A list can be Initialized with a comma-separated list of values.

:examplebase: creating_lists
<div style="page-break-after: always"></div>

## Indexing and slicing
****
* Use brackets for index
* Use slice for multiple values
* Same syntax for strings, lists, and tuples
****

Python is very flexible in selecting elements from a list. All selections are done by putting an index or a range of indices in square brackets after the list's name.

To get a single element, specify the index (0-based) of the element in square brackets:
<div style="page-break-after: always"></div>

ifdef::highlight[]
[source,python]
endif::highlight[]
----
foo =  [ "apple", "banana", "cherry", "date", "elderberry",
   "fig","grape" ]

foo[1]  the 2nd element of list foo -- banana
----

To get more than one element, use a slice, which specifies the beginning element (inclusive) and the ending element (exclusive):

ifdef::highlight[]
[source,python]
endif::highlight[]
----
foo[2:5]    foo[2], foo[3], foo[4] but NOT foo[5] – cherry, date, elderberry
----

If you omit the starting index of a slice, it defaults to 0:

ifdef::highlight[]
[source,python]
endif::highlight[]
----
foo[:5] foo[0], foo[1], foo[2], foo[3], foo[4] – apple,banana,cherry, date, elderberry
----

If you omit the end element, it defaults to the length of the list.

ifdef::highlight[]
[source,python]
endif::highlight[]
----
foo[4:] foo[4], foo[5], foo[6] – elderberry, fig, grape
----
A negative offset is subtracted from the length of the list, so -1 is the last element of the list, and -2 is the next-to-the-last element of the list, and so forth:

ifdef::highlight[]
[source,python]
endif::highlight[]
----
foo[-1] foo[len(foo)-1] or foo[6] – grape
foo[-3] foo[len(foo)-3] or foo[4] – elderberry
----

The general syntax for a slice is

ifdef::highlight[]
[source,python]
endif::highlight[]
----
s[start:stop:step]
----

which  means all elements s[N], where 

   start <= N < stop, 

and start is incremented by step

TIP: Remember that start is **IN**clusive but stop is **EX**clusive.

(((indexing))) (((slicing)))

ifdef::instructor[]
[instructor-heading]*Instructor Note*
[instructor-text]#Slide: *_Slices_*.#
endif::instructor[]

ifndef::ebook-format[<<<]

=## Example

:examplebase: indexing_and_slicing
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----

ifndef::ebook-format[<<<]

include::{exampledir}callouts/{examplebase}.callouts[]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile}]


ifndef::ebook-format[<<<]

## Iterating through a sequence
****
* use a **for** loop
* works with lists, tuples, strings, or any other iterable
* Syntax

----
 for var in iterable:
     statement
     statement
     ...
----

****

To iterate through the values of a list, use the *for* statement.  The variable takes on each value in the sequence, and keeps the value of the last item when the loop has finished.

To exit the loop early, use the break statement. To skip the remainder of an iteration, and return to the top of the loop, use the continue statement.

*for* loops can be used with any iterable object.

TIP: The loop variable retains the last value it was set to in the loop even after the loop is finished. (If the loop is in a function, the loop variable is local; otherwise, it is global).

(((iterating through a sequence))) (((for loop)))

ifndef::ebook-format[<<<]


=## Example

:examplebase: iterating_over_arrays
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----
include::{exampledir}callouts/{examplebase}.callouts[]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile}]

ifndef::ebook-format[<<<]

<div style="page-break-after: always"></div>
## Tuples (((tuples)))
****
* Designed for "records" or "structs"
* Immutable (read-only)
* Create with comma-separated list of objects
* Use for fixed-size collections of related objects
* Indexing, slicing, etc. are same as lists
****

Python has a second array type, the *tuple*. It is something like a list, but is immutable; that is, you cannot change values in a tuple after it has been created.

A tuple in Python is used for "records" or "structs" -- collections of related items. You do not typically iterate over a tuple; it is more likely that you access elements individually, or _unpack_ the tuple into variables. 

Tuples are especially appropriate for functions that need to return multiple values; they can also be good for passing function arguments with multiple values.

While both tuples and lists can be used for any data, there are some conventions. 

* Use a list when you have a collection of similar objects. 
* Use a tuple when you have a collection of related, but dissimilar objects. 

In a tuple, the position of elements is important; in a list, the position is not important.

For example, you might have a list of dates, where each date was contained in a month, day, year tuple.

To specify a one-element tuple, use a trailing comma; to specify an empty tuple, use empty parentheses. 

----
result = 5,
result = ()
----

TIP: Parentheses are not needed around a tuple unless the tuple is nested in a larger data structure. 


ifndef::ebook-format[<<<]

=## Example

:examplebase: creating_tuples
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile}]

> __TIP__: To specify a one-element tuple, use a trailing comma, otherwise it will be interpreted as a single object:

ifdef::highlight[]
[source,python]
endif::highlight[]
----
color = 'red',
----

ifdef::instructor[]
[instructor-heading]*Instructor Note*

[instructor-text]#It's important to emphasize that a tuple is designed for unpacking or directly indexing, and that it is not just a less useful version of a list.#

[instructor-text]#Slide: *_Lists vs Tuples_*.#

endif::instructor[]

====

ifndef::ebook-format[<<<]

## Iterable Unpacking
****
* Copy elements to variables
* Works with any array-like object
* More readable than numeric indexing
****

If you have a tuple like this:

----
my_date = 8, 1, 2014
----

You can access the elements with 

----
print(my_date[0], my_date[1], my_date[2])
----

It's not very readable though. How do you know which is the month and 
which is the day?

A better approach is _unpacking_, which is simply copying a tuple (or any other ((iterable)){empty}) to a list of variables:

----
month, day, year = my_date
----

Now you can use the variables and anyone reading the code will know what they mean. This is really how tuples were designed to be used. 


ifdef::instructor[]
[instructor-heading]*Instructor Note*
[instructor-text]#If the class is interested, you can show them extended unpacking.#
endif::instructor[]

(((tuple unpacking)))


ifndef::ebook-format[<<<]

## Nested sequences
****
* Lists and tuples may contain other lists and tuples
* Use multiple brackets to specify higher dimensions
* Depth of nesting limited only by memory
****

Lists and tuples can contain any type of data, so a two-dimensional array can be created using a list of lists. A typical real-life scenario consists of reading data into a list of tuples. 

There are many combinations – lists of tuples, lists of lists, etc. 

To initialize a nested data structure, use nested brackets and parentheses, as needed.

(((nested sequences)))

ifndef::ebook-format[<<<]

=## Example

:examplebase: nested_sequences
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----
include::{exampledir}callouts/{examplebase}.callouts[]

ifndef::ebook-format[<<<]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile}]

ifndef::ebook-format[<<<]

## Functions for all sequences
****
* Many builtin functions expect a sequence
* Syntax
****

ifdef::highlight[]
[source,python]
endif::highlight[]
----
    n = len(s)
    n = min(s)
    n = max(s)
    n = sum(s)
    s2 = sorted(s)
    s2 = reversed(s)
    s = zip(s1,s2,...)
----

Many builtin functions accept a sequence as the parameter. These functions can be applied to a list, tuple, dictionary, or set.

*len(s)* returns the number of elements in s (the number of characters in a string).

*min(s)* and *max(s)* return the smallest and largest values in s. Types in s must be similar -- mixing strings and numbers will raise an error.

*sorted(s)* returns a sorted list of any sequence s. 

NOTE: min(), max(), and sorted() accept a named parameter *key*, which specifies a key function for converting each element of s to the value wanted for comparison. In other words, the key function could convert all strings to lower case, or provide one property of an object. 

*sum(s)* returns the sum of all elements of s, which must all be numeric.

*reversed(s)* returns an iterator (not a list) that can loop through s in reverse order. 

*zip(s1,s2,...)* returns an iterator consisting of  (s1[0],s2[0]),(s1[1], s2[1]), ...). This can be used to "pivot" rows and columns of data. 

(((sequence functions)))
(((**len()**))) (((**min()**))) (((**max()**))) (((**sum()**)))
(((**sorted()**))) (((**reversed()**))) (((**zip()**)))

ifndef::ebook-format[<<<]

=## Example

:examplebase: sequence_functions
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----
include::{exampledir}callouts/{examplebase}.callouts[]

ifndef::ebook-format[<<<]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile}]

ifndef::ebook-format[<<<]

## Using enumerate()
****
* Numbers items beginning with 0 (or specified value)
* Returns enumerate object that provides a _virtual_ list of tuples
****

To get the index of each list item, use the builtin function enumerate(s). It returns an *enumerate object*. 

ifdef::highlight[]
[source,python]
endif::highlight[]
----
for t in enumerate(s):
    print(t[0],t[1])

for i,item in enumerate(s):
    print(i,item)

for i,item in enumerate(s,1)
    print(i,item)
----

When you iterate through the following list with enumerate():

----
    [x,y,z]
----

you get this (virtual) list of tuples:

----
    [(0,x),(1,y),(2,z)]
----

You can give enumerate() a second argument, which is added to the index. This way you can start numbering at 1, or any other place.
(((enumerate())))

ifdef::instructor[]
[instructor-heading]*Instructor Note*

[instructor-text]#Discuss collections vs. virtual lists here, so students can learn that enumerate(), reverse(),  open(), zip(), etc. return generators.#

[instructor-text]#Slide: *_enumerate()_*.#

[instructor-text]#Slide: *_Iterables_*.#

endif::instructor[]

ifndef::ebook-format[<<<]

=## Example

:examplebase: enumerate
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----
include::{exampledir}callouts/{examplebase}.callouts[]

ifndef::ebook-format[<<<]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile}]

ifndef::ebook-format[<<<]

## Operators and keywords for sequences
****
* Operators +   *
* Keywords  *del*   *in*   **not in**
****

*del* deletes an entire string, list, or tuple. It can also delete one element, or a slice, from a list. del cannot remove elements of strings and tuples, because they are immutable.

*in* returns True if the specified object is an element of the sequence.

*not in* returns True if the specified object is _not_ an element of the sequence.

*+*  adds one sequence to another

*{splat}* multiplies a sequence (i.e., makes a bigger sequence by repeating the original).

(((in))) 

ifdef::highlight[]
[source,python]
endif::highlight[]
----
    x in s  #note – x can be any Python object
    s2 = s1 * 3
    s3 = s1 + s2
----

ifndef::ebook-format[<<<]

=## Example

:examplebase: sequence_operators
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----
include::{exampledir}callouts/{examplebase}.callouts[]

ifndef::ebook-format[<<<]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile}]

ifndef::ebook-format[<<<]

## The range() function (((range{lparen}{rparen})))
****
* Provides (virtual) list of numbers
* Slice-like parameters
* Syntax
ifdef::highlight[]
[source,python]
endif::highlight[]
----
    range(stop)
    range(start, stop)
    range(start, stop, step)
----
****

The range() function returns a **range object**, that provides a list of numbers when iterated over. The parameters to range() are similar to the parameters for slicing (start, stop, step).

This can be useful to execute some code a fixed number of times. 


ifndef::ebook-format[<<<]

=## Example

:examplebase: using_ranges
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----
include::{exampledir}callouts/{examplebase}.callouts[]

ifndef::ebook-format[<<<]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile}]

ifndef::ebook-format[<<<]

## List comprehensions (((list comprehension)))
****
* Shortcut for a for loop
* Optional if clause
* Always returns list
* Syntax
----
[ EXPR for VAR in SEQUENCE if EXPR ]
----
****

A list comprehension is a Python idiom that creates a shortcut for a for loop. A loop like this:

ifdef::highlight[]
[source,python]
endif::highlight[]
----
results = []
for var in sequence:
    results.append(expr)   # where expr involves var
----

can be rewritten as

ifdef::highlight[]
[source,python]
endif::highlight[]
----
results = [ expr for var in sequence ]
----

A conditional if may be added:

ifdef::highlight[]
[source,python]
endif::highlight[]
----
results = [ expr for var in sequence if expr ]
----

The loop expression can be  a tuple. 
You can nest two or more for loops.

ifndef::ebook-format[<<<]

=## Example

:examplebase: list_comprehensions
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----

ifndef::ebook-format[<<<]

include::{exampledir}callouts/{examplebase}.callouts[]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {exampledir}{examplefile} | head -30]

__etc etc__

ifndef::ebook-format[<<<]

## Generator Expressions (((generator expressions)))
****
* Similar to list comprehensions
* Lazy evaluations – only execute as needed
* Syntax
----
( EXPR for VAR in SEQUENCE if EXPR )
----
****

A generator expression is very similar to a list comprehension. There are two major differences, one visible and one invisible. 

The visible difference is that generator expressions are created with parentheses rather than square brackets. The invisible difference is that instead of returning a list, they return an iterable object. 

The object only fetches each item as requested, and if you stop partway through the sequence; it never fetches the remaining items. Generator expressions are thus frugal with memory. 

ifndef::ebook-format[<<<]

=## Example

:examplebase: generator_expressions
:examplefile: {examplebase}.py

*{examplefile}*

ifdef::highlight[]
[source,python]
endif::highlight[]
----
include::{exampledir}{examplefile}[]
----

include::{exampledir}callouts/{examplebase}.callouts[]

ifndef::ebook-format[<<<]

*_{examplefile}_*

capture::[cd {exampledir} && {python3exe} {examplefile}]


ifdef::instructor[]
[instructor-heading]*Instructor Note*

[instructor-text]#This is a good place to talk about collections vs. generators.#

[instructor-text]#Slide: *_Iterables_*.#
endif::instructor[]

// leave page break before labs for both PDF and EPUB

<<<

[float]
## Chapter {chapternum} Exercises

:!labnum:

=## Exercise {chapternum}-{counter:labnum} (pow2.py)

Print out all the powers of 2 from 2^0^ through 2^31^. 

Use the ** operator, which raises a number to a power. 

NOTE: For exercises {chapternum}-2 and {chapternum}-3, start with the file sequences.py, which has the lists ctemps and fruits already typed in.  You can put all the answers in sequences.py

=## Exercise {chapternum}-{counter:labnum} (sequences.py)

*ctemps* is a list of Celsius temperatures. Loop through ctemps, convert each temperature to Fahrenheit, and print out both temperatures. 

=## Exercise {chapternum}-{counter:labnum} (sequences.py) 
Use a list comprehension to copy the list *fruits* to a new list named *clean_fruits*, with all fruits in lower case and leading/trailing white space removed. Print out the new list.

HINT: Use chained methods  (x.spam().ham())

ifndef::ebook-format[<<<]

=## Exercise {chapternum}-{counter:labnum} (sieve.py)

__FOR ADVANCED STUDENTS__

The "Sieve of Eratosthenes" is an ancient algorithm for finding prime numbers. It works by starting at 2 and checking each number up to a specified limit. If the number has been marked as non-prime, it is skipped. Otherwise, it is prime, so it is output, and all its multiples are marked as non-prime.

Write a program  to implement this algorithm. Specify the limit (the highest number to check) on the script's command line. Supply a default if no limit is specified.

Initialize a list (maybe named *is_prime*) to the size of the limit plus one (use * to multiply a single-item list). All elements should be set to *True*.

Use two _nested_ loops. 

The outer loop will check each value (element of the array) from 2 to the upper limit. (use the `range()`) function. 

If the element has a *True* value (is prime),  print out its value. Then, execute a second loop iterates through all the multiples of the number, and marks them as *False* (i.e., non-prime). 


No action is needed if the value is False. This will skip the non-prime numbers.

TIP: Use range() to generate the multiples of the current number.

NOTE: In this exercise, the _value_ of the element is either *True* or *False* -- the _index_ is the number be checked for primeness.

_See next page for the pseudocode for this program:_

ifdef::instructor[]
[instructor-heading]*Instructor Note*
[instructor-text]#The sieve exercise (for advanced students) might require a bit of whiteboarding to explain.#
endif::instructor[]

ifndef::ebook-format[<<<]

=## Pseudocode for sieve.py

----
if # command line args ## 1
    get LIMIT from command line
else
    set LIMIT to 50

Initialize IS_PRIMES list to size LIMIT+1, with all TRUE values

for NUM  from 2 to LIMIT+1
    if IS_PRIME[NUM]
        output NUM
        for M from NUM to LIMIT+1, counting by NUM
            IS_PRIME[M] = FALSE
----


// vim: set syntax=asciidoc:

