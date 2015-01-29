
madlib = '''on the first day of code guild, a ________ came into the course to discuss _________.
the students asked how best to _________ when the code goes _________.'''

print madlib

noun1 = raw_input("enter a noun: ")
noun2 = raw_input("enter a noun: ")
verb = raw_input("enter a verb: ")
adverb = raw_input("enter an adverb: ")

var='''In the first day of code guild, a {} came into the course to discuss {}.
\n the students asked how best to {} when the code goes {}.'''

print var.format(noun1,noun2,verb,adverb)