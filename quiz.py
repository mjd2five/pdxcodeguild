print "Hello World"
list = ['apples', 'oranges', 'bananas']
print list
list[1] = 'grapes'
print list

people = {
	"Bob": {'name': 'Bob', 'age': '22'},
	"Carol": {'name': 'Carol', 'age': '47'},
	"Justin": {'name': 'Justin', 'age': '14'}
	}

number_1 = int(input("what is the first number? : "))
number_2 = int(input("what is the second number? : "))
print "The first number is %d, the second number is %d, and the new number is %d" % (number_1, number_2, (number_1 + number_2))

def uptok():
	numero = int(input("What is your number? : "))
	while numero < 1000:
		numero += 5
		print numero
uptok()

x = 0
while x < 100:
	print x
	x += 1
	print x
	x += 1
	print x
	print 'fizz'
	x += 2
	print x
	print 'buzz'
	x += 1

class customer:
	def __init__(self, name, age, location, credit_score):
		self.name = name
		self.age = age
		self.location = 'Washington'
		self.credit_score = 718
		

		name = 'Jessie'
		print name
		print location
		print credit_score
		self.credit_score = 750
		print credit_score

customer()