1.
Question 1

In Python, which data type represents text?
.

str

complex

int

float

2.
Question 2

Given the string Name="ABCDE", what outcome does the operation Name.find("B") produce?
.

2

0

5

1

3.
Question 3

What following code segment would produce an output of “0”?
.

2//1

2/1

1//2

1/2

4.
Question 4

Complete the statement. Dictionary items can be:
.

Only one data type

Numerous data types

Stored in duplicate keys

A collection of strings only

5.
Question 5

What is the syntax to obtain the first element of the tuple?

A=('a','b','c')
.

A[-1]

A[:]

A[0]

A[1]

6.
Question 6

What does the split() method return from a list of words?
.

 A list of substrings split based on a specified delimiter (or whitespace by default).  

 A list of substrings in reverse order.  

 A single string of words separated by colons.  

 A single long string with the words joined by a delimiter.  

7.
Question 7

If A is a list, what happens with this segment of code: a=set(A)?
.

It returns an ordered list.

It casts the list “a” to the set “A”

It returns an error

It casts the list “A” to the set “a”

8.
Question 8

For the code shared below, what value of x will produce the output “How are you?”? [Select three]

```python

if(x!=1): 
    print('How are you?') 
else: 
    print('Hi') 
```
.

x = 6

x = 0

x = 1

x = "7"

9.
Question 9

Which statement ensures the execution of the remaining code regardless of the outcome?
.

If

Finally

For

While

10.
Question 10

For the provided add function below, what is the return value of the following?
```python 
def add(x):
    return(x + x)
add('1')
```
.

'11'

'2'

2

Error

11.
Question 11

What is the output of the following?
```python
for i in range(1,5): 
      if (i!=2):  
          print(i)
```

1. 
    2 

2. 
    1

    3

    4
3.
    1

    3

    4

    5
4.
    1

    2

    3

    4

12.
Question 12

Which method in the Rectangle class draws the rectangle?
```python
class Rectangle(object): 

  def __init__(self,width=2,height =3,color='r'):

    self.height=height 

    self.width=width 

    self.color=color 

  def drawRectangle(self): 

    import matplotlib.pyplot as plt 

    plt.gca().add_patch(plt.Rectangle((0, 0),self.width, self.height ,fc=self.color)) 

    plt.axis('scaled') plt.show()
```

drawRectangle

import matplotlib

class Rectangle

__init__

13.
Question 13

What function returns a sorted list?
.

sort()

sorted()

lower()

find()

14.
Question 14

What outcome do the following lines of code produce?

a=np.array([0,1,0,1,0]) 

b=np.array([1,0,1,0,1]) 

a/b 

.

array([0, 0, 0, 0, 0])

array([0.1, 1.0, 0.1, 1.0, 0.1])

array([1, 1, 1, 1, 1])

Division by zero error

15.
Question 15

What outcome do the following lines of code produce?

a=np.array([10,9,8,7,6]) 

a+1

.

array([101,91,81,71,61])

array([9, 8, 7, 6, 5])

array([11,10,9,8,7])

array([110,19,18,17,16])

16.
Question 16

What does the following line of code select along with the headers ‘Artist’, ‘Length’, ‘Year’ and ‘Genre’ from the dataframe df?

y=df[['Artist','Length','Genre']]
.

The specified Columns

The entire dataframe

The specified column headers only.

The specified Rows

17.
Question 17

Given the file object named file1, which of the following codes prints the first 2 lines of the content in it?
.
```python
for n in range(0, 2):

    print(file1.readline())
```

file1.readline(2)

file1.read(2)

file1.readline(4) 

18.
Question 18

Which line of code is in the mode of append?
.

with open("Example.txt","r") as file1:

with open("Example.txt","w") as file1:

with open("Example.txt","a") as file1:

with open("Example.txt","wb") as file1:

19.
Question 19

What is scheme, internet address and route a part of?
.

Text file

URL

API

Error message

20.
Question 20

What is the process of extraction of data from a website called?
.

Crowd sourcing

Web crawling

Data mining

Webscraping