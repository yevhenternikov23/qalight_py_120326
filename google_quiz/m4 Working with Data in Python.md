1.
Question 1

What is the outcome of the following lines of code?

a=np.array([-1,1]) b=np.array([1,1]) np.dot(a,b)
.

array([0,2]) 

0 

array([[-1, -1], [1, 1]]) 

1 
 
2.
Question 2

What is the first step you must check before performing matrix multiplication between two NumPy arrays A and B?
.

Both arrays must be square matrices.

The sum of the dimensions must be even. 

The number of columns in A must equal the number of rows in B. 

The arrays must have the same shape. 
 
3.
Question 3

What does the attribute ndim return when applied to the following NumPy array?

X=np.array([[1,0,1],[2,2,2]]) X.ndim
.

2 

3 

5 

6 
 
4.
Question 4

When used between two NumPy arrays, what mathematical operation does the asterisk (*) perform?
.

Matrix multiplication 

Element-wise multiplication (Hadamard product) 

Scalar multiplication 

Element-wise addition 
 
5.
Question 5

Consider the following text file: Example1.txt: This is line 1 This is line 2 This is line 3

What is the output of the following lines of code?

with open("Example1.txt","r") as file1: FileContent=file1.read() print(FileContent)
.

This is line 1 This is line 2 This is line 3 

This is line 1 This is line 2 

This is line 1 

This 
 
6.
Question 6

When would you use the “a” mode with the open() function?
.

When you want to read from a file 

When you want to create a completely new file 

When you want to overwrite an existing file 

When you want to add content to an existing file without overwriting it 
 
7.
Question 7

What do the following lines of code do?

with open("Example.txt","w") as writefile: writefile.write("This is line A\n") writefile.write("This is line B\n")
.

Create a binary file "Example.txt" 

Append the file "Example.txt" 

Write to the file "Example.txt" 

Read the file "Example.txt" 
 
8.
Question 8

What is the difference between the “w” and “a” modes when opening a file?
.

“w” creates new files only, “a” modifies existing files only 

“w” is for writing binary files, “a” is for writing text files 

“w” is faster but less secure than “a” 

“w” overwrites the file while “a” adds to the end of the file 
 
9.
Question 9

What's the difference between loc and iloc methods in pandas?
.

loc uses labels for indexing, while iloc uses integer positions 

loc is faster than iloc for large datasets 

loc is used for rows, iloc is used for columns 

loc can only access single cells, while iloc can slice rows and columns 
 
10.
Question 10

What function would you use to load a CSV file in Pandas?
.

pd.load_csv(path) 

pd.read_excel(path) 

pd.read_csv(path) 

np.read_csv(path) 