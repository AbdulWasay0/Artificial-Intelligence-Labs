Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
1/2
0.5
#Comments in Python
2 ** 3
8
#That was exponent
#Now for division
17/3
5.666666666666667
#floor division
17//3
5
#moculus operator
23%3
2
#subtraction of numbers
5-3
2
5+9
14
5*6
30
#for Printing any thing using print function
print("Hello")
Hello

#now by making a variable
v=1
print("The Value of v is:",v)
The Value of v is: 1
v = v+1
print ("V is now equal to itself plus 1",v)
V is now equal to itself plus 1 2
v
2
#Now making the integer 5 times
v = v * 5
print ("The value of v now will be : ",v)
The value of v now will be :  10

#now for string
word1 = "Good"
word2 = "Morning"
print (word1, word2)
Good Morning
sentence = word1 + " " + word2
print (sentence)
Good Morning

#using Rational Operators in Pyhton
#less than
print (5 < 7)
True
#greater than
print (10 > 3)
True
#less than equal
print (5 <= 5)
True
#Greater than
print (10 >= 30)
False
#not equal
print (5 != 5)
False
#equal to
print (4 == 4)
True

#Now using Boolean Logic in Python
#if - condition
a = 3
if a > 2
SyntaxError: expected ':'


#Now using Boolean Logic in Python
#if - condition
a = 4
if a > 3:
    print ("a is greater than 3: ")

    
a is greater than 3: 
#if-else condition
    
a=3
if a == 4:
    print("a is equal")
else:
    print ("Not Equal")
... 
...     
Not Equal
>>> 
>>> #if--else-if--else condtion in one
>>> result = 87
>>> if result >= 90
SyntaxError: expected ':'
>>> if result >= 90
SyntaxError: expected ':'
>>> 
>>> #if--else-if--else condtion in one
>>> result = 87
>>> if result >= 90:
...     print ("Grade: A")
... elif result >= 80:
...     print ("Grade: B")
... elif result >= 70:
...     print ("Grade: C")
... elif reuslt >= 60:
...     print ("Grade: D")
... else:
...     print ("Failed")
... 
...     
Grade: B
>>> 
>>> #Lab Journal 1-B
>>> x = input("Please enter an integer: ") 
... if x < 0: 
... x = 0 
... print('Negative changed to zero') 
... elif x == 0: 
... print('Zero') 
... elif x == 1: 
... print('Single') 
... else: 
... print('More') 
... 
SyntaxError: multiple statements found while compiling a single statement
>>> 

>>> #Lab Journal 1-B
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 5
>>> 
