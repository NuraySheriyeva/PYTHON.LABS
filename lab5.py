import re as r

# that matches a string that has an 'a' followed by zero or more 'b''s.
print("1")
t=input("ENter: ")
x=r.search(r"^ab*", t)

if x:
    print("MATCH")
else:
    print("NO MATCH")
# that matches a string that has an 'a' followed by two to three 'b'.
print("2")
t=input("ENter: ")
x=r.search(r"^ab{2,3}", t)

if x:
    print("MATCH")
else:
    print("NO MATCH")
# to find sequences of lowercase letters joined with a underscore.
print("3")
t=input("ENter: ")
x=r.search(r"[a-z]+_[a-z]+", t)

if x:
    print("MATCH")
else:
    print("NO MATCH")
# to find the sequences of one upper case letter followed by lower case letters.
print("4")
t=input("ENter: ")
x=r.search(r"[A-Z][a-z]+", t)

if x:
    print("MATCH")
else:
    print("NO MATCH")
# that matches a string that has an 'a' followed by anything, ending in 'b'.
print("5")
t=input("ENter: ")
x=r.search(r"a.*b$", t)

if x:
    print("MATCH")
else:
    print("NO MATCH")
# to replace all occurrences of space, comma, or dot with a colon.
print("6")
t=input("ENter: ")
x=r.sub(r"[ ,.]", ":", t)
print(x)
# to convert snake case string to camel case string.
print("7")
t = input("Enter: ")
x =  r.sub(r"_([a-z])", lambda m: m.group(1).upper(), t)
print(x)
# to split a string at uppercase letters.
print("8")
t=input("Enter: ")
x=r.split("[A-Z]", t)
print(x)
# to insert spaces between words starting with capital letters.
print("9")
t = input("Enter: ")
x = r.sub(r'([a-z])([A-Z])', r'\1 \2', t)
print(x)
# to convert a given camel case string to snake case.
print("10")
t = input("Enter: ")
x = r.sub(r"([a-z])([A-Z])", r"\1_\2", t )
x = r.sub(r"([A-Z])", lambda m: m.group(1).lower(), x)
print(x)
'''
import re as r

t="The rain in Spain"
x=r.search("^The.*Spain$", t)

if x:
    print("1")
else:
    print("2")

#findall()  returns a list containing all matches, 
#           if none - empty list
x=r.findall ("ai", t)
print(x) 
 
#search()   returns a Match object if there is a 
#           match anywhere in the string. if more than one,
#           only first occurence returns
x=r.search("T", t)
print("First T is at:", x.start()) #<-- empathis on start()

#split()    returns a list where the string has been
#           split at each match
x=r.split("n", t, 2) #2 being how many times it will be done
print(x)

#sub()      replaces the matches with the text of your choice
x=r.sub("\s", "9", t, 2) #2 beign how many times it will be done
print(x)

#match object is an object containing information about the search and the result
#   if there is no match, 'None' will be returned
x=r.search("ai", t)
print(x)
#   Match object has methods to get info about searches, results:
#   span()      returns a tuple containing the start&end positions of match
x=r.search(r"\bS\w+", t)
print(x.span())
#   string      returns the string passed into the function
print(x.string) #prints the sentence t, in the beginning
#   group()     returns the part if the string where there was a match
print(x.group()) #prints words that start with S
'''
'''
[]	alphabetically target char between a&m	"[a-m]"	
\	Signals special characters	"\d" (here is digits)	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group

\A	 if the specified characters are at the beginning of the string	"\AThe"	
\b	 where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" r"ain\b"	
\B	 where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"	

\d	contains digits (numbers from 0-9)	"\d"	
\D	DOES NOT contain digits	"\D"	
\s	contains a white space character	"\s"	
\S	DOES NOT contain a white space character	"\S"	
\w	contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
'''