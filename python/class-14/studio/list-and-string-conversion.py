proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for string in strings:
    if ',' in string:
        print('The list ' + string + ' has commas')
    elif ';' in string:
        print('The list ' + string + ' has semicolons')
    elif ' ' in string:
        print('The list ' + string + ' has spaces')
    else:
        print('nothing')
# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
for string in strings:
    if ',' in string:
        comma = string.split(',')
        comma.reverse()
        rcommastr = ','.join(comma)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
    elif ';' in string:
        semicolon = string.split(';')
        semicolon.sort()
        rsemicolonstr = ';'.join(semicolon)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
    elif ' ' in string:
        spaces = string.split(' ')
        spaces.sort(reverse=True)
        rspacesstr = ' '.join(spaces)
# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
else:
        commaspaces = string.split(', ')
        commaspaces.reverse()
        rcommaspacesstr = ', '.join(commaspaces)

print(rcommastr)
print(rsemicolonstr)
print(rspacesstr)
print(rcommaspacesstr)