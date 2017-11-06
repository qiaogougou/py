# Filename: if.py

number = 23
# guess = int(raw_input('Enter an integer:'))  # python 2
guess = int(input('Enter an integer:')) # python 3

if guess == number:
	print('Congratulations, you guessed it.')
elif guess < number:
	print('No, it is a little higher than that')
else:
	print('No, it is a little lower than that')
print('Done')