########################################################################
#This is open source project for people to learn basic concept about 
#python and contribute work for others. You will find some new concept 
#as well as complex syntax like generator mapping etc.
########################################################################




#This is the first comment

spam = 1  # and this is the second comment
text = '# This is not a comment because it's a inside qutoes.'

#Using Python as a Calculator

#Numbers
2+2 #output 4

50 - 5 * 6 # output 20

(50 - 5 * 6 ) # outpur 5.0

8/5 # output 1.6 | Division always return a floating point number.

17 / 3 # classic division returns  float | output 5.6666666.

17 // 3 # floor division discards the fractional part.

17 % 3 # The % operaor returns the remainder of the division.

#With python, it's possibile to use the ** operator to calculate powers

5 ** 2 # 2 5 to the power of 2 | outpur 25

#Variables 
#use last output values to get new output by using _ symbol
firstNumber = 20
lastNumber = 30
firstNumber + lastNumber #output 50
firstNumber + _ #output 70


myFirstName = "Ankit"
myLastName = "Kumar"
#We can concatenate two variable by using + symbol
myFirstName + myLastName #output AnkitKumar

#Strings
print('This is single quotes')
print("This is double quotes')
print('You\'re not authorize') #We can use single quote inside single quote by applying \ before single quotes inside those quotes
print("\"You are\",not authorized")

#3 times word 
print('hello*3) # Output hellohellohello

# You can concatenate two string directly without using + symbol
'Hello' 'World'

#if you want to break long sting
print("Hello this is first line"
    "This is end of line")

#String can be indexed
word = 'Python'
word[0] # Character at position 0 willbe "P"

#We can slice string by using : symbol
word[0:2] # 0 is starting point and 2 is ending point | output will be "Pyt"

#We have to make sure that s[:i] + s[i:] is equal to s
word[:2] + word[2:] # Output will be "Python"

#Indexing concept
'''

 +---+---+---+---+---+---+
|  P | Y | T | H | O | N |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1   
 
 '''
 
 #You can find the lnegth of the word by using len() funcion, This is built in function
 s = "helloworldthisistesting"
 len(s) # output 22
 
 
