### Regular Expressions
- Regex is a way to match patterns in text
- You need to import the module re to use the regex functions
- search takes in a regex pattern and a string and returns true if the pattern is found in the string
- ^ matches the beginning of a string
- . matches any character
```
^F..m: - matches any string that starts with an F and has m as the 4th character
```
- + and * indicate repeated characters
- Use findall() to extract all substrings that match a pattern
- Square brackets indicate multiple acceptable characters
- \S matches any non-whitespace character
- Parentheses indicate where to extract the substring
- Regex can be used to both search and extract information
- Escape characters with \ to match special characters
- . inside square brackets matches a literal period and outside matches any character

### Summary
```
^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
```

### Extra
- grep is a command on linux/unix that lets you run regex commands on files
- help() is a python command used to help find information about a function or module. Just pass the function or module name as a parameter and get information about it.

### Glossary
- brittle code: code that breaks easily if you make a small change to the correct input
- greedy matching: the default behavior of the + and * operators where they match as much text as possible
- wild card: a special character that matches any character