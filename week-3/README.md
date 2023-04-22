# Week - 3

## Regular Expressions

```
 . - means anything
eg: d.k = { dork, desk, duck, ... }

 ^ - 'starts with' anchor tag
eg: ^a = { assassin, anchor, apple, ... }

 $ - 'ends with' anchor tag
eg: y$ = { sunny, day, hey, dany, ... }
 
```
## Basic Regular Expressions

> Simple Matching in Python

```py
import re

# Here 'r' means raw string
result = re.search(r'aza','plaza')
print(result)
# output: <re.Match object; span(2, 5), match='aza'>

result = re.search(r'aza','bazaar')
print(result)
# output: <re.Match object; span(1, 4), match='aza'>

result = re.search(r'aza','Luke')
print(result)
# output: None

result = re.search(r'^L','Luke')
print(result)
# output: <re.Match object; span(0, 1), match='L'>

re.search(r'<regex_expr>','<input_str>',re.IGNORECASE)
# where 're.IGNORECASE' is used to be case insensitive
```

> Wildcards and Character Classes

```py
import re

re.search(r'[Pp]ython','Python')
re.search(r'[Pp]ython','python')
# both the statements returns same output
# the wildcard character '[]' is used to consider the character place with the square brackets

re.search(r'[a-z]','<input_str>')         # We accept all small alphabetical characters
re.search(r'[A-Z]','<input_str>')         # We accept all capital alphabetical characters
re.search(r'[0-9]','<input_str>')         # We accept all numerical characters
re.search(r'[a-zA-Z]','<input_str>')      # We accept all alphabetical characters
re.search(r'[a-zA-Z0-9]','<input_str>')   # We accept all alphanumerical characters

# [^] acts oppsite of []
re.search(r'[^a-z]','<input_str>')         # We accept anything except small alphabetical characters
re.search(r'[^A-Z]','<input_str>')         # We accept anything except capital alphabetical characters
re.search(r'[^0-9]','<input_str>')         # We accept anything except numerical characters
re.search(r'[^a-zA-Z]','<input_str>')      # We accept anything except alphabetical characters
re.search(r'[^a-zA-Z0-9]','<input_str>')   # We accept anything except alphanumerical characters

# | a.k.a pipe character is used as 'or' operation
re.search(r'this|that','<input_str>')      # Accepts everything which contains either 'this' or 'that' words

# findall returns all possible matched patterns found
re.findall(r'this|that','<input_str>')     # returns all matched found in the given string
```

> Repetition Qualifiers

```py
import re

# '*' will accept everything including nothing, this is called greedy behaviour.
re.search(r'start.*end','<input_str>')     # this will accept the strings which start with 'start' word and has anything or even nothing in between and ends with 'end' word.
# eg: { 'start is not the end', 'start at 9:30 and then end', 'startend' } are some example which is accepted by above statement.

# '+' is similar to '*' but it should be present atleast once in the string.
re.search(r'start+end+','<input_str>')     # this will accept the strings which start with 'start' word and has anything or even nothing in between and ends with 'end' word.
# eg: { 'startstartend', 'startendend', 'startend' } are some example which is accepted by above statement.

# '?' will accept either a single occurence or nothing
re.search(r'once?.*','<input_str>')         # this will accept the strings which start with single occurence of word 'once' or not even occurence of word 'once'.
# eg: { 'once upon a time', 'once', '', 'upon a time' } are some example which is accepted by above statement.
```

> Escaping Characters

```py
import re

# We use '\' to specify that the special (or) wildcard character are actually part of pattern string.
re.search(r'\.com$','<input_str>')         # accepts all strings which ends with '.com' word.
# eg: { 'www.google.com', 'gmail.com', '.com' }

# '\w' is used to accept all the alphanumeric characters including underscore
re.search(r'\w+','<input_str>')            # accepts all strings which has atleast one occurence of alphanumeric and underscore character
# eg: { 'abcd', '0123', 'Hello_world_123', 'hi123' }

# similar to '\w', '\d' accepts only numeric characeters.
re.search(r'\d*','<input_str>')            # accepts all strings which has any number of occurences of numeric digits including nothing
# eg: { '1246', '' }

# similarily '\s' accepts only white space characters.
re.search(r'\s+','<input_str>')            # accepts all strings which has atleast one occurence of whitespace
# eg: { ' ', '   ', '\t', '\n', '\t \n' }
```

> Regular Expressions in Action

```py
import re

# we must add starting and ending anchor tags to make it more strict.
# Say if we want to find whether the given country name starts and endswith 'a'.
print( re.search(r'[aA].*a','Argentina') != None )      # Output: True
print( re.search(r'[aA].*a','Azerbaijan') != None )     # Output: True

# But we though this regex expr will give us the countries whose name starts and endswith 'a'.
# This happened because our regex expr match the country name 'Azerbaijan' till 'Azerbaija', thus it result as True

# To avoid such problems we should make our regex expr more strict by adding starting and ending anchor tags.
# Hence the modified and corrected answer for the above problem is:
re.search(r'^[aA].*a$', '<input_country_name>')

```
