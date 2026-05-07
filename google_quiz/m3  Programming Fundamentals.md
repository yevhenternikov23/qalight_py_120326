1.
Question 1

A traffic management system uses the following code to control pedestrian crossing signals:

signal_state = "Red"
if signal_state == "Green":
    print("Walk")
else:
    print("Wait")
print("Look both ways")

What message will pedestrians see on the display?
.

Walk Wait

Wait Look both ways 

Walk Look both ways 

Look both ways
 
2.
Question 2

Which of the following is the true value of x after the following lines of code?

x = 1 
x = x > 5
.

x=1

x=5 

x=-1

False
 
3.
Question 3

A file download progress tracker uses the following code to show the percentage remaining:

remaining_percent = 100
while remaining_percent > 25:
    print(f"{remaining_percent}% remaining")
    remaining_percent = remaining_percent-25

What will be displayed to the user during this download?
.

100% remaining

100% remaining 75% remaining 50% remaining

100% remaining 75% remaining 50% remaining 25% remaining

100% remaining 75% remaining 50% remaining 25% remaining 0% remaining
 
4.
Question 4

What is the result of running the following lines of code?

class Points(object):
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 
p1 = Points("A", "B") 
p1.print_point()
.

y=B 

x=A y=B 

x=y= 

x=A 
 
5.
Question 5

What fundamental capability does the enumerate() function provide that a standard loop does not?
.

It limits iteration to only specific elements that meet certain criteria. 

It allows loops to process elements in reverse order. 

It automatically tracks both the index position and element value simultaneously. 

It makes loops execute faster by pre-computing all values. 
 
6.
Question 6

A weather application uses a class to track temperature data. What will be displayed when this code is running?

class WeatherData:
    def __init__(self, temp_c, humidity):
        self.temp_c = temp_c
        self.humidity = humidity
    def display(self):
        print(f"Temperature: {self.temp_c}°C, Humidity: {self.humidity}%")
today = WeatherData(22, 45)
today.temp_c = 25
today.display()
.

Error: Cannot modify object attributes after creation 

Temperature: (22, 25)°C, Humidity: 45% 

Temperature: 25°C, Humidity: 45% 

Temperature: 22°C, Humidity: 45% 
 
7.
Question 7

A data validation system uses a function to check if a value falls within an acceptable range. What will the following function return when processing a sensor reading of 32?

def validate_temperature(reading): 
    if 20 <= reading <= 40: 
        result = "Valid" 
    else: 
        result = "Invalid" 
return result
.

“Invalid” 

“Valid” 

False 

None 
 
8.
Question 8

What is the output of the following line of code?

a = 1 
def do(x): 
    a = 100 
    return x + a 
print(do(1))
.

102 

101 

2 

1 
 
9.
Question 9

Which function definition demonstrates the most efficient implementation for adding two numbers? 
.

Direct return of parameter summation 

Built-in sum function with tuple conversion

Intermediate variable assignment before return 

Built-in sum function with individual parameters 
 
10.
Question 10

A data analysis program processes financial records using the following code:

try: 
    file = open('financial_data.csv', 'r') 
    data = file.read() 
    result = process_data(data) 
    print(f"Total: ${result}") 
except FileNotFoundError: 
    print("Error: Financial data file not found.") 
except ValueError: 
    print("Error: Data contains invalid values.") 
finally: 
    file.close()

What is the benefit of using specific error types rather than a single generic block?
.

The program will run faster with specific error types. 

Multiple blocks are required by Python syntax. 

Different errors can be handled with appropriate, specific responses. 

The program will use less memory. 