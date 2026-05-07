1.
Question 1

Which statement accurately describes the relationship between tuples and lists in Python?
.

Elements in nested tuples cannot be accessed using multiple indices. 

Tuples can contain lists, but lists cannot contain tuples. 

Tuples and lists cannot be nested within each other. 

Tuples can contain lists, and lists can contain tuples. 
 
2.
Question 2

Consider the tuple A=((1),[2,3],[4]), that contains a tuple and list. What is the result of the following operation A[2]?
.

3 

1 

[4] 

[2,3] 
 
3.
Question 3

The method append does the following:
.

Creates a new list with an added element 

Adds one element to a list 

Adds multiple elements to a list 

Merges two lists 
 
4.
Question 4

Consider the following list: A=["hard rock",10,1.2] What will list A contain after the following command is run? del(A[1])
.

["hard rock",1.2] 

["hard rock",10] 

[10,1.2] 

Syntax error 
 
5.
Question 5

What is the importance of creating proper copies of lists in Python rather than using direct assignment?
.

Direct assignment is deprecated in recent Python versions. 

Proper copies use less memory than direct assignment. 

List copying is only necessary when working with numeric data. 

Changes to a copied list will not affect the original list, while changes to an assigned list will. 
 
6.
Question 6

What is the outcome of the following? len(("disco",10,1.2, "hard rock",10))
.

6 

0 

7 

5 
 
7.
Question 7

A music streaming service stores album release years in a dictionary: album_years = {"Thriller":"1982", "Back in Black":"1980", "The Dark Side of the Moon":"1973"}. When generating a "Years in Music" report, which elements from this dictionary should be extracted?
.

"1982", "1980", "1973"

Both the album names and years together 

The dictionary structure itself

"Thriller", "Back in Black", "The Dark Side of the Moon" 
 
8.
Question 8

Which statement accurately describes how to add or update an entry in a Python dictionary?
.

Dictionaries are immutable and cannot be modified after creation.

Use the insert() method to add new entries at specific positions. 

Use square bracket notation with the key to assign or update its value. 

Use the add() method to insert new key-value pairs. 
 
9.
Question 9

A data analyst is tracking unique website visitors. The current visitors set is visitors = {'user123', 'user456'}. A new visitor with ID 'user789' visits the site. What will the visitors set contain after executing visitors.add('user789')?
.

{'user123', 'user456'}

{'user789', 'user123', 'user456'} 

{'user123', 'user456', 'user789', 'user789'} 

Error 
 
10.
Question 10

A security system maintains a set of authorized access codes: auth_codes = {'A123', 'B456', 'C789'}. When someone enters code 'B456', which Python expression would the system use to verify if this is an authorized code?
.

'B456' in auth_codes 

auth_codes == 'B456' 

auth_codes.contains('B456')

auth_codes.find('B456') 