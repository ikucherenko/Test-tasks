#!/usr/bin/python3

# Task №1
def handle_numbers(start, end, divisible):
	count = 0
	for num in range(start, end+1):
		if num%divisible == 0:
			count+=1
	return count


print(handle_numbers(1,10,2))