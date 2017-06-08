#!/usr/bin/python3


# Task №2
def handle_string(word):
	l = 0
	d = 0
	for letter in word:
		if letter.isdigit():
			d+=1
		elif letter.isalpha():
			l+=1
	return l, d

letters,digits = handle_string("Hello world!123!")
print("Letters={0} Digits={1}".format(letters, digits))