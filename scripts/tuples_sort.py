#!/usr/bin/python3

from operator import itemgetter

def handle_list_of_tuples(tuples):

	sorted_by_name = sorted(tuples)
	return sorted(sorted_by_name, key=itemgetter(1,2,3), reverse=True)
	
	
tuples = [
("Tom", "19", "167", "54"),
("Jony", "24", "180", "69"),
("Json", "21", "185", "75"),
("John", "27", "190", "87"),
("Jony", "24", "191", "98"),
]

sorted_list = handle_list_of_tuples(tuples)

for item in sorted_list:
	print(item)