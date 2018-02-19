Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myint=7
>>> print(myint)
7
>>> myfloat=7.0
>>> print(myfloat)
7.0
>>> myfloat=float(7)
>>> print()

>>> myfloat=float(9)
>>> print(myfloat)
9.0
>>> myint=int(22)
\
>>> print(myint)
22
>>> mystring="it is simple one"
>>> print(mystring)
it is simple one
>>> one=1
>>> two=2
>>> three=one+two
>>> print(three)
3
>>> hello="hello"
>>> world="world"
>>> helloworld=hello+world
>>> print(helloworld)
helloworld
>>> hello="hello"
>>> world="world"
>>> print(hello+world)
helloworld
>>> 
=============================== RESTART: Shell ===============================
>>> hello="hello"
>>> world="World"
>>> print(hello+world)
helloWorld
>>> print(helloworld)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(helloworld)
NameError: name 'helloworld' is not defined
>>> print(hello+" "+world)
hello World
>>> 
=============================== RESTART: Shell ===============================
>>> one = int (1)
two = int (2)
hello = "hello"

print(one + two + hello)
SyntaxError: multiple statements found while compiling a single statement
>>> one = 1
two =  2
hello = "hello"

print(one + two + hello)
SyntaxError: multiple statements found while compiling a single statement
>>> one = int (1)
two = int (2)
hello = "hello"

print(one ,two + hello)
SyntaxError: multiple statements found while compiling a single statement
>>> one = int (1)
two = int (2)
hello = "hello"

print(one + two )
SyntaxError: multiple statements found while compiling a single statement
>>> one = int (1)
two = float(2)
hello = "hello"

print(one + two + hello)
SyntaxError: multiple statements found while compiling a single statement
>>> one = int (1)
#two = int (2)
hello = "hello"

print(one + two + hello)
SyntaxError: multiple statements found while compiling a single statement
>>> 
KeyboardInterrupt
>>> #one = int (1)
#two = int (2)
hello = "hello"

print(one + two + hello)
SyntaxError: multiple statements found while compiling a single statement
>>> one = int (1)
two = int (2)
hello = "hello"

print(one + two )
SyntaxError: multiple statements found while compiling a single statement
>>> 
KeyboardInterrupt
>>> one = int (12)
#two = int (2)
hello = "hello"

print(one )
SyntaxError: multiple statements found while compiling a single statement
>>> 
=============================== RESTART: Shell ===============================
>>> one = int (1)


print(one + two + hello)
SyntaxError: multiple statements found while compiling a single statement
>>> 
KeyboardInterrupt
>>> one = int (1)
two = int (2)
hello = "hello"

print(one )
SyntaxError: multiple statements found while compiling a single statement
>>> mylist=[1,2,3]
>>> print(mylist[0])
1
>>> print(mylist[2])
3
>>> print(mylist[3])
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(mylist[3])
IndexError: list index out of range
>>> 
=============================== RESTART: Shell ===============================
>>> mylist=[]
>>> mylist.append(1)
>>> mylist.append(2)
>>> mylist.append(1)
>>> print(mylist[2])
1
>>> print(mylist[0])
1
>>> print(mylist[1])
2
>>> 
=============================== RESTART: Shell ===============================
>>> number=[]
>>> strings=[]
>>> number.append(1)
>>> number.append(2)
>>> number.append(343)
>>> strings.append("hello")
>>> strings.append(" ")
>>> strings.append("world")
>>> second_name= number[2]
>>> print(number)
[1, 2, 343]
>>> print(strings)
['hello', ' ', 'world']
>>> string.append('')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    string.append('')
NameError: name 'string' is not defined
>>> strings.append('')
>>> print(strings)
['hello', ' ', 'world', '']
>>> print("the second name on the name list is %d"%second_name)
the second name on the name list is 343
>>>  print("the second name on the name list is %s"%second_name)
 
SyntaxError: unexpected indent
>>>  print("the second name on the name list is %d"%second_name)
 
SyntaxError: unexpected indent
>>>  print("the second name on the name list is %d"%second_name)
 
SyntaxError: unexpected indent
>>> print("the second name on the name list is %d"%second_name)
the second name on the name list is 343
>>>  print("the second name on the name list is %d"%second_name)
 
SyntaxError: unexpected indent
>>> lotsofhellos = "hello" * 10
print(lotsofhellos)
SyntaxError: multiple statements found while compiling a single statement
>>> lotsofhellos = "hello" * 10
print(lotsofhellos)
SyntaxError: multiple statements found while compiling a single statement
>>> lots="hello"*10
>>> print(lots)
hellohellohellohellohellohellohellohellohellohello
>>> prints(lots /n)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    prints(lots /n)
NameError: name 'prints' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> name="home"
>>> print("%s#"%name)
home#
>>> name1=john
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    name1=john
NameError: name 'john' is not defined
>>> name1="john"
>>> print("%s3"%name1,"%s2"%name)
john3 home2
>>> name2=int(2)
>>> print("%s"%name1,"%d"%name2)
john 2
>>> name3=float(55)
>>> print("%s"%name1,"%d"%name2,"%f"%name3)
john 2 55.000000
>>> 
=============================== RESTART: Shell ===============================
>>> mylist=[1,2,3]
>>> print("A list:%s"%mylist)
A list:[1, 2, 3]
>>> 
=============================== RESTART: Shell ===============================
>>> data=("john","doe",45.55)
>>> format_string="heloo %s is %s .your current balance is %f"
>>> print(format_string)
heloo %s is %s .your current balance is %f
>>> print(format_string % data)
heloo john is doe .your current balance is 45.550000
>>> print(format_string)
heloo %s is %s .your current balance is %f
>>> format_string="heloo %s is %s .your current balance is %s"
>>> print(format_string%data)
heloo john is doe .your current balance is 45.55
>>> 
=============================== RESTART: Shell ===============================
>>> for x in range(5)
SyntaxError: invalid syntax
>>> for x in range(5):
	print(x)

0
1
2
3
4
>>> for x in range(2,9)
SyntaxError: invalid syntax
>>> for x in range(2,9):
	print(x)

	
2
3
4
5
6
7
8
>>> for x in range(2,22,2)
SyntaxError: invalid syntax
>>> for x in range(2,22,2):
	print(x)

	
2
4
6
8
10
12
14
16
18
20
>>> for x in range(2,22,2):
	for y in range(1,11,2):
		print(y)

		
1
3
5
7
9
1
3
5
7
9
1
3
5
7
9
1
3
5
7
9
1
3
5
7
9
1
3
5
7
9
1
3
5
7
9
1
3
5
7
9
1
3
5
7
9
1
3
5
7
9
>>> for x in range(2,22,2):
	for y in range(1,11,2):
		print(y)
		print(x)

		
1
2
3
2
5
2
7
2
9
2
1
4
3
4
5
4
7
4
9
4
1
6
3
6
5
6
7
6
9
6
1
8
3
8
5
8
7
8
9
8
1
10
3
10
5
10
7
10
9
10
1
12
3
12
5
12
7
12
9
12
1
14
3
14
5
14
7
14
9
14
1
16
3
16
5
16
7
16
9
16
1
18
3
18
5
18
7
18
9
18
1
20
3
20
5
20
7
20
9
20
>>> count=0
>>> 
=============================== RESTART: Shell ===============================
>>> count=0
>>> while count<5:
	print(count)
	count+=1

	
0
1
2
3
4
>>> count=0
>>> while count<=5
SyntaxError: invalid syntax
>>> while count<=0:
	print(count)
	count+=1

	
0
>>> count=0
>>> while count<=5:
	print(count)
	count+=1
	
SyntaxError: multiple statements found while compiling a single statement
>>> count=0
>>> while count<=5
SyntaxError: invalid syntax
>>> while count<6
SyntaxError: invalid syntax
>>> count=0
>>> while count<6:
	print(count)
	count+=1

	
0
1
2
3
4
5
>>> 
=============================== RESTART: Shell ===============================
>>> def my_function():
    print("Hello From My Function!")

    
>>> 
>>> def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

    
>>> 
========== RESTART: C:\Users\Admin\Desktop\python programs\test2.py ==========
>>> hh
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    hh
NameError: name 'hh' is not defined
>>> hhhh
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    hhhh
NameError: name 'hhhh' is not defined
>>> username
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    username
NameError: name 'username' is not defined
>>> def my_function():
    print("Hello From My Function!")

    
>>> my_function()
Hello From My Function!
>>> def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

    
>>> my_function_with_args("John Doe", "a great year!")
Hello, John Doe , From My Function!, I wish you a great year!
>>> 
=============================== RESTART: Shell ===============================
>>> class Student:  
   def __init__(self, rollno, name):  
      self.rollno = rollno  
      self.name = name  
   def displayStudent(self):  
      print "rollno : ", self.rollno,  ", name: ", self.name  
emp1 = Student(121, "Ajeet")  
emp2 = Student(122, "Sonoo")  
emp1.displayStudent()  
emp2.displayStudent()
SyntaxError: Missing parentheses in call to 'print'
>>> 
