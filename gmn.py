# This is a guess the number game.
import random

isPlaying = True
while isPlaying:
	guessesTaken = 0
	number = random.randint(1, 20)
	print('I am thinking of a number between 1 and 20.')

	isGuessing = True
	while isGuessing:
		print('Take a guess.') # There are four spaces in front of print.
		guess = input()
		guess = int(guess)

		guessesTaken = guessesTaken + 1
		if guess < number:
			print('Your guess is too low.') # There are eight spaces in front of print.
		if guess > number:
			print('Your guess is too high.')
		if guess == number:
			break
			
	print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
	print('Want to play again? (y|n)')
	temp = input()
	temp = str(temp).lower()
	if temp != 'y':
		isPlaying = False