#Basics of Python Assignment

#.1   Explain the key features of Python that make it a popular choice for programming.    
     
# >>> The key features of Python that make it a popular choice for programming  are following -:
#     1. Python is an interactive and interpreted language with simple syntax.
#     2. It is directly executed with pre-compiled code.it is already compiled by the interpreter at  the runtime.
#     3. It is loosely typed OOP language with few keywords and  simple english like structure.
#     4. Python is easy to read and understand its code for beginners .

#___________________________________________________________________________________________________________________


# .2   Describe the role of predefined keywords in Python and provide examples of how they are used in a program

# >>> A keyword in python is a word that serves a specific function in Python. It is limited to one single 
#     function and it can not be set as a variable name, a function name, or the value of any other 
#     identifier. The purpose of the keyword is to define the syntax of the code.

#     for example-
#     print --> it is an pre-defined keyword that has only one specific purpose i.e tp print anything given 
#     to function 
#     for eg.
#      print("hello world")  

#      similar to that there are more keywords that are reserved in python that cant be used as variable name 
#      some of which are
#      True , False, none, and ,break, for, while, etc
#      
#      We can get the list of predefined keywords in python by using this  code
#      {
#          import keyword
#          print(keyword.kwlist)
#      }
#      This code will give list of ever pre-defined keyword in python.

#---------------------------------------------------------------------------------------------------------------------
# .3    Compare and contrast mutable and immutable objects in Python with examples
#    >>>  a mutable object allows you to modify its internal state after creation means we can change its
#       value at the runtime.whereas
#       immutable objects doesn't allows you to modify its internal state after creation means its value can't
#       be changed 
#       example of mutable objects are  
#       list, dictionary

#       example of immutable objects are
#       tuples,strings,sets,numbers,booleans

#       example of mutable objects-:
#           {
#               digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#               print (digits[3])
#               digits[3]= 19
#               print(digits)
#                           }
#      example if immutable objects-:
#           {
#              name="parixit singh"
#              print(name)
#              print(name[5])
#              name[5]="r"
#              print(name)
#                           }

#-------------------------------------------------------------------------------------------------
# 4.   Discuss the different types of operators in Python and provide examples of how they are used
#  >>>  operators are special symbols or keywords that carry out operations on values and python variables.
#       They serve as a basis for expressions, which are used to modify data and execute computations.
#       Python contains several operators, each with its unique purpose
#       different types of operators that are used in python are -:
#       Arithmetic Operators-> used for athematic operations like addition(+), subtraction(-), multiplication(*) and division(/)
#       and some special types of athematic operators are modulo(%) also called remainder and floor division(//)
#       for example
#               {
#               a = 21
#               b = 10
#               # Addition
#               print ("a + b : ", a + b)
#               # Subtraction
#               print ("a - b : ", a - b)
#               # Multiplication
#               print ("a * b : ", a * b)
#               # Division
#               print ("a / b : ", a / b)
#               # Modulus
#               print ("a % b : ", a % b)
#               # Exponent
#               print ("a ** b : ", a ** b)
#               # Floor Division
#               print ("a // b : ", a // b)
#                           }

#       
#       Comparison (Relational) Operators-> are used To compare two values, Python comparison operators are needed.
#       Based on the comparison, they produce a Boolean value (True or False).
#       comparison operators are equal(=), not equal(!=),greater than(>),Less Than(<),Greater Than or Equal to(>=)
#       etc,
#       for example
#                   a = 4
#                   b = 5
                    # Equal
#                   print ("a == b : ", a == b)
#                   # Not Equal
#                   print ("a != b : ", a != b)
#                   # Greater Than
#                   print ("a > b : ", a > b)
#                   # Less Than
#                   print ("a < b : ", a < b)
#                   # Greater Than or Equal to
#                   print ("a >= b : ", a >= b)
#                   # Less Than or Equal to
#                   print ("a <= b : ", a <= b)

#       
#       Logical Operators--> logical operators are used to compose Boolean expressions and evaluate their truth values.
#       They are required for the creation of conditional statements as well as for managing the flow of execution in programs.
#       Python has three basic logical operators: AND, OR, and NOT.
#       for eg;
#                           x = 5
#                           y = 10
#                           if x > 3 and y < 15:
#                             print("Both x and y are within the specified range")

#       Bitwise Operators--> # Python bitwise operators execute operations on individual bits of binary integers.
#       They work with integer binary representations, performing logical operations on each bit location.
#       Python includes various bitwise operators, such as AND (&), OR (|), NOT (), XOR (), left shift (), and right shift (>>).


#       Membership Operators--> membership operators are used to determine whether or not a certain value occurs within a sequence.
#       They make it simple to determine the membership of elements in various Python data structures such as lists, tuples, sets, and strings.
#       Python has two primary membership operators: the in and not in operators.
#       for example;
#                       numbers = [1,2,3]
#                       if 0 in fruits:
#                           print("Yes, 0 is in number sequence!")
#                       else:
#                           print("No, 0 is not in the number sequence!")
# --------------------------------------------------------------------------------------------------------------------------

# 5.  Explain the concept of type casting in Python with example
#    >>> TypeCasting, also known as type conversion, is a process that converts a variable’s data type into another data type.
#        These conversions can be implicit (automatically interpreted) or explicit (using built-in functions).
#       there are two types of typecasting process in python  
#       1.Implicit Type-casting-> In implicit type-casting Python interpreter automatically performs type conversion
#           on some operations without any user involvement.
#           for example;
#                           y =2
#                           print(type(y))
#                           y=y+2.2
#                           print(type(y))



#       2. Explicit Type-casting  --> Explicit type casting involves Python’s predefined functions that act as a constructor of another data type
#           The str() function takes an integer or float as an argument and converts it to a string.
#           The int() function takes a string or float as an argument converts it to an integer.
#           The float() function takes an integer or string as an argument and converts it to a float.
#           for example;
#                                    x=5
#                                    print(type(x))
#                                    x=float(x)
#                                    print(type((x)))

#-----------------------------------------------------------------------------------------------------------------------------------

# 6.    How do conditional statements work in Python? Illustrate with examples
#  >>>> Conditional Statements are statements in Python that provide a choice for the control flow based on a condition.
#       It means that the control flow of the Python program will be decided based on the outcome of the condition
#       there are four types of conditional or decision making statements in python that are;
    #   1. if statement-> It is the easiest method of design making  in python .It simply states that if something is true or not.
#       for example:
#           x=5
#           if(x==5):
#              print("the value of x is 5")


#       2. if-else statement--> In a conditional if Statement the additional block of code is merged as an else statement which is performed when if condition is false. 
#          for example:
#                               age=18
#                               if(age==18):
#                                   print("you are eligible to vote-")
#                               else:
#                                   print("you are not eligible to vote")


#       3. if-elif ladder--> The if statements are executed from the top down. 
#           As soon as one of the conditions controlling the if is true, the statement associated with that if is
#           executed, and the rest of the ladder is bypassed. 
#           If none of the conditions is true, then the final “else” statement will be executed.
#                           names=["parixit", "harry", "prince"]
#                           print(names)
#                           name=input("\nenter your name from the above list\n")
#                           if(name==names[0]):
#                               print("your name is ",names[0])
#                           elif(name==names[1]):
#                               print("your name is ", names[2])
#                           elif(name==names[2]):
#                               print("your name is ", names[3])
#                           else:
#                               print("invalid!!! \nplease enter names only from list provided")

#       4. nested if-else statements--> Nested if..else means an if-else statement inside another if statement.
#           Or in simple words first, there is an outer if statement, and inside it another
#           if – else statement is present and such type of statement is known as nested if statement.
#           We can use one if or else if statement inside another if or else if statements.
#           for example:
# if..else chain statement
#                            letter = "A"
#                           if letter == "B":
#                               print("letter is B")
#                           else:
#                               if letter == "C":
#                                   print("letter is C")

#                               else:
#                                   if letter == "A":
#                                       print("letter is A")

#                                   else:
#                                       print("letter isn't A, B and C")

#--------------------------------------------------------------------------------------------------------------------

# 7. Describe the different types of loops in Python and their use cases with examples.
# >>> A loop is an instruction that repeats multiple times as long as some condition is met
#       there are two types of loops in python
#       1.for loop  -> A for loop in Python is used to iterate over a sequence
#           for example:
#                                   x="parixit"
#                                   for i in x:
#                                       print(i)


#       2.while loop  -> The while loop is used to execute a set of statements as long as a condition is true.
#           for example:
#   	                         x=5
#   	                         i=0
#   	                         while(x>i):
#   	                             print("hello world")
#   	                             i +=1