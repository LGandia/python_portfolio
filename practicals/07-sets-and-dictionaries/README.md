# Week 7
## Task 1
Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].

## Task 2
Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:

- Letters that appear in at least one of the two words.
- Letters that appear in both words.
- Letters that appear in either word, but not in bot

_Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line._

## Task 3
Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise, it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).

_Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on._

## Task 4
One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.

Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.

_Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes._