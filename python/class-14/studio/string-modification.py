my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
first3 = my_string[:3]
leftover = my_string[3:]
newstr = leftover + first3
print(newstr)

# Use a template literal to print the original and modified string in a descriptive phrase.
""" print('The original string is {my_string} and the new string is {newstr}.') """

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
default_input = int(input('How many letters should I remove from the front and add to the end? Please choose a number within the index range: '))

if default_input < 0 or default_input > len(my_string):
    default_input = 3
    defaultnote = "As you used an illegal input, we have set your input to 3."
else:
    first3 = my_string[:default_input]
    leftover = my_string[default_input:]
    newstr = leftover + first3
    defaultnote = ""

print(newstr)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

print('{}The original string is {} and the new string is {}.'.format(defaultnote,my_string, newstr))