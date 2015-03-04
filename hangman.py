import random


class game():    #setting up the word banks based on the level
	def __init__(self):
		selection = int(input("Choose your ability level: "))
		if selection == 1:
			self.word_list = ['thrust', 'flood']
			self.guess_total = 14
			hangman_game(self)
		elif selection == 2:
			self.word_list = ['biscuit', 'hollow']
			self.guess_total = 12
			hangman_game(self)
		elif selection == 3:
			self.word_list = ['I love pizza', 'turtle power']
			self.guess_total = 10
			hangman_game(self)
		elif selection == 4:
			self.word_list = ['life is best out west', 'all the world is a stage']
			self.guess_total = 8
			hangman_game(self)
		else:
			print "Let's try that again...."
			game()

#def hangman_game(self):
#	random_word = random.choice(word_list)
#	mask = []
#	for i in random_word:
#			mask.append("_")
	#while guess_total < game.guess_total     #error for some reason
#	print "keep guessing; number remaining: "
#	print game.guess_total
#	letter = raw_input("choose a letter: ")
#	if letter in random_word:     #"letter" not defined
#		print "nice selection!"
#	print random_word
#if letter not in random_word:
#	print "sorry, no dice..."
#	print random_word
def guess(self):
	print "guess a letter: "
	guessed_letter = raw_input("").strip.lower()
	self.possible_guesses = ["X" if letter == guessed_letter else letter for letter in self.possible_guesses]
	if guessed_letter not in word.letter_list:
		self.wrong_guesses.append(guessed_letter)
		print "sorry, that letter returned nothing"


def play():                       
	print "1) Beginner"
 	print "		4-5 letter words, 14 incorrect guesses"
 	print "2) Intermediate"
 	print "		6+ letter words, 12 incorrect guesses"
 	print "3) Advanced"
	print "		2-3 word phrases, 10 incorrect guesses"
	print "4) Expert"
	print "		3+ word phrases, 8 incorrect guesses"
	game()

play()

#different levels with different word/phrase banks and amount of guesses
#def beginner():
#	while (len(wrong) <= 14):    #loop the process
#		guess = input("pick a letter: ")
#		if guess not in beginner_word:  #beginner_word references 
#			len(wrong) += 1
#			print "you have " + str(len(wrong)) + "guesses remaining."
#	if len (wrong) == 15:
#		print "You are out of guesses.  The word was: "
#		print beginner_word

