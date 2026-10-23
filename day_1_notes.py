name = input("Enter your Name:   ") # Define your terms, preferably avoid any capital letters in lines of code not intended for direct printing
age = int(input("Enter your Age (+1):   "))- 1 # Use input to request for user iformation directly, the '-1' is a mathematical equation that runs after the value is inputed, the equation will not work unless the value inside is converted to an interger (whole number or other numerical value)
# PAY ATTENTION TO THE COLOUR OF THE BRACKETS, POSITIONING, NUMBER OF THEM AND TYPES USED
department = input("Enter your Department:   ")# whatever is written inside must be closed in quaations, either single or double
favorite_course = input("Enter your Favourite Course:   ") # use underscore("_") when connecting two words in code not a dash(-) unless it's relevant to the code
hobby = input('Enter your Hobby:   ') 
 # leave it bank to leave a space
print('=================Basic Student Profile==================') # use print to write out lines of code  
print()
print(f'My name is {name}') #the f string is a different way of writing prrinted stuff, most times preferable
# this space doesnt addd any value to the code, its to help make your work look neater
print()
print(f'I am {age} years old')
print()
print(f'I am in {department} Department ')
print()
print(f'My favourite course is {favorite_course}')
print()
print(f'I enjoy {hobby}')
print()