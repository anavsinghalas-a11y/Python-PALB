#1. the sum of 1 to 5  is 15 :

print("The sum of 1 to 5 is:", 1+2+3+4+5)

#02-01 .he figure below is a flowchart of a program that finds the sum of odd numbers among integers between 1 and 100 and 
 #prints the sum. Fill in the blanks in the second figure of the following flowchart.

N = 1
S = 0

while N <= 100:
    S = S + N
    N = N + 2

print("Sum of odd numbers between 1 and 100 is:", S)

#02-02. we will write a program that receives a positive integer from the user and tells whether it is an odd or even number. 
#Complete the appropriate pseudo code for the underlined part.

print("Enter an integer:")
n = int(input())

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

#03-01 Write a code to print the following decorative output. In the first line, use only one '*' character with the operator * and 
#number. In the second line, use only one '#' character and one space with the operator * and number.
#Coding guideline: In the case of the first line, print in the same way as '*' * number n. The second line also uses the * 
#operator.

n = 30   # you can change this number

# First line using only one '*' character
print('*' * n)

# Second line using one '#' and one space
print('# ' * n)

#04-01 Write and save the following name and address in the name and address variables, respectively. Write a code that 
#prints them to the screen.

name = "David Doe"
address = "1600 Wilshire Blvd #205, Los Angeles CA 90017"

print(name)
print(address)

#05-01 Expect the output of the following code and write it down.

x = 1
y = 0
print(x and y) # output 0
print(x or y) # output 1
print(not x)  # ouput false
print(not y)  #ouput true 

#6-1 Write a program that takes two random integers as input and lists them from smallest to largest.
#(Condition: Two integers are not the same number.)

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

if num1 < num2:
    print(num1, num2)
else:
    print(num2, num1)

 #07-01  Write a program that performs the following using a compound conditional expression of an if statement.
#Coding guideline: Write a code that performs differently depending on whether the answer to the first question is 0 or 1, 
#as shown below.

adult = int(input("Are you an adult? (1 if you are an adult, 0 if you are minor): "))
married = int(input("Are you married? (1 if you are married, 0 if you are single): "))

if adult == 1 and married == 1:
    print("You are an adult who is married.")
elif adult == 1 and married == 0:
    print("You are an adult who is single.")
elif adult == 0 and married == 1:
    print("You are a minor who is married.")
else:
    print("You are a minor who is single.")


#8-01 Among the positive natural numbers other than 1, a number that is not prime is called a composite number. Print the 
#prime and composite numbers from 2 to 12 as follows.
#Coding guideline: Use the for statement to solve this problem. When using a nested for statement, an expression for 
#determining a prime number must be entered in the inner for statement

for num in range(2, 13):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, ": Prime number")
    else:
        print(num, ": Composite number")

#9-01 An Armstrong number is a three-digit integer that is equal to the sum of the cubes of each digit. Find all Armstrong 
#numbers among three-digit integers and print them as follows.
         
print("Three-digit Armstrong numbers:", end=" ")

for num in range(100, 1000):   # Loop from 100 to 999
    original_num = num
    result = 0

    while original_num != 0:
        remainder = original_num % 10    
        result += remainder ** 3           
        original_num //= 10               

    if result == num:
        print(num, end=" ")         

#10-01 If there are two lists l1 and l2 with the following strings, use the combination of l1 and l2 to print as follows.

l1 = ['I like', 'I love']
l2 = ['pancake.', 'kiwi juice.', 'espresso.']

for i in l1:         
    for j in l2:      
        print(i, j)  

#11-01  The person dictionary is defined as follows. Add a new item to this person dictionary with the key 'Father' and the value 
#'John Doe'. And then print the person dictionary.          

person = {
    'Name': 'David Doe',
    'Age': 26,
    'Weight': 82,
    'Job': 'Data scientist'
}

# Adding new item
person['Father'] = 'John Doe'

# Printing dictionary
print(person)

#12-01 With tuple data, the values of two variables can be swapped without using a temporary variable. Using this swapping 
#method, write a program that moves the largest value in the given list to the last.

lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

# Find index of the largest value
max_index = 0
for i in range(len(lst)):
    if lst[i] > lst[max_index]:
        max_index = i

# Swap largest value with the last element using tuple swap
lst[max_index], lst[-1] = lst[-1], lst[max_index]

print(lst)

#13-01 The two-dimensional array a contains the values [[1, 2], [3, 4], [5, 6]]. Change this two-dimensional array to a one
#dimensional array like [1, 2, 3, 4, 5, 6], and print it out

a = [[1, 2], [3, 4], [5, 6]]

one_d = []          # new empty list

for row in a:       # loop through each inner list
    for value in row:
        one_d.append(value)

print(one_d)

#14 There is a dictionary variable mariaas follows. In this dictionary variable, courses such as ‘korean' and ‘english' and their 
 #scores are stored as key:value. Print the average score of 89.25 for maria'ssubject scores.

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

# Get all the scores using values()
scores = maria.values()

# Calculate average
average = sum(scores) / len(scores)

print(average)

#15 declare a nested dictionary school as follows. Next, use the deepcopy() function of the copy module to write a program 
#that 'copy' to another variable, school2. (Check that school and school2are different variables through the is operator.)
 
import copy

school = {
    'kim': {'age': 16, 'hei': 170, 'grade': 3},
    'lee': {'age': 15, 'hei': 168, 'grade': 2},
    'choi': {'age': 14, 'hei': 173, 'grade': 1}
}

# Deep copy
school2 = copy.deepcopy(school)

# Check if both are different objects
print(school is school2)

#16 There is a scores tuple as follows. This tuple contains information about four students, including each student's name 
#and English, math, and science grades. For example, ‘Hyun’ has an English score of 88, a math score of 95, and a science 
#score of 90. Extract only math scores by unpacking the scores tuple. Write a code that calculates the average of these 
#extracted math scores.

scores = (
    ('Hyun', 88, 95, 90),
    ('Kang', 85, 90, 95),
    ('Park', 70, 90, 80),
    ('Hong', 90, 90, 95)
)

# Use zip to unpack: names, english, math, science
names, eng, math, sci = zip(*scores)

# Calculate math average
average_math = sum(math) / len(math)

print(average_math)
