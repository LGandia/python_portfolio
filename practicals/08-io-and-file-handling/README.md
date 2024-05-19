# Week 8
## Task 1
The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for dry runs or white-box
testing). Write an implementation of this command. It should take the name of the
files as a command-line argument.

## Task 2
The Unix diff command compares two files and reports the differences, if any.
Write a simple implementation of this that takes two file names as command-line
arguments and reports whether or not the two files are the same. (Define "same" as
having the same contents.)

## Task 3
The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string.

## Task 4
The Unix wc command counts the number of lines, words, and characters in a file.
Write an implementation of this that takes a file name as a command-line
argument, and then prints the number of lines and characters.
_Note: Linux (and Mac) users can use the "wc" command to check the results of their
implementation._

## Task 5
The Unix spell command is a simple spell-checker. It prints out all the words in a
text file that are not found in a dictionary. Write and test an implementation of this,
that takes a file name as a command-line argument.

_Note: You may want to simplify the program at first by testing with a text file that
does not contain any punctuation. A complete version should obviously be able to
handle normal files, with punctuation._

_Another Note: You will need a list of valid words. Linux users will already have one
(probably in /usr/share/dict/words). It is more complicated, as usual, for
Windows users. Happily, there are several available on GitHub_
