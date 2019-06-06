#This study-related project.
#The main goal of it is to build plot with month of birth(as y axial) and name of a person(as x axial).

import json # For storing data. It is acceptable with little amount of data.
from collections import Counter # Needs for additional purpose. Counts number of each month of birth.
from bokeh.plotting import figure, show, output_file #builds plot

#opens main file with data
with open('info.json', 'r') as file:
	file = json.load(file)
	
print('Welcome to the Birthday database!')


#Shows who already exists in the file
def print_person(persons):
	for person in persons:
		print(person)
print('We have these people birthdays: ')
print_person(file)
pers = str(input("Who's birthday do you want to know?> "))
pers = pers.capitalize()
if pers in file.keys():
	print(f"{pers} birthday is {file[pers]}")
else:
	print('This person does not exist in the database!')

#add new person to the main file
def add_new_person(person, birth_db):
	birth_db.update(person)
	
	with open('info.json', 'w') as new_file:
		json.dump(birth_db, new_file)

user_ans = str(input('Would you like to add new person to this list? '))

#user decides whether he\she wants to add someone(if yes, user inputs required data) 
if user_ans.lower() == 'yes':
	pers_name = str(input("Input person's name: "))
	pers_birthday = str(input("Input person's birthday: "))
	person = {pers_name: pers_birthday}
	add_new_person(person, file)
else:
	print()

dates = file.values()
months_of_birth = []
for date in dates:
	months_of_birth.append(int(date.split('/')[1]))

#The folowing code builds reversed dict for better manipulating and searching through the data
name_of_month = ['January', 'February', 'March', 'April', 'May',
		     'June', 'July', 'August', 'September', 'October',
		     'November', 'December']

num_of_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months_range = dict(zip(num_of_month, name_of_month))

#Additional options. You can count months and spreading of each month among list of persons.
# new_month_list = []

# for mon in months_of_birth:
# 	new_month_list.append(months_range[mon])

# con = Counter(new_month_list)
# con = json.dumps(con, indent=4, sort_keys=True)


#Builds datalist for x, and y axis
def build_plot(file: dict, months_range: dict) -> 'html':
	x = []
	y = []
	date_of_birth = list(file.values())
	y_categories = list(months_range.values()) #values of data presented in y(vertical) axis
	x_categories = list(file.keys()) #values of data presented in x(gorizontal) axis
	for k, v in file.items():# generates data to build plot
		x.append(k)
		y.append(months_range[int(v.split('/')[1])])
	
	output_file('birthday_plot.html')
	p = figure(x_range=x_categories, y_range=y_categories)
	p.circle(x=x, y=y, color='blue', size=10, alpha=0.5)
	show(p)

if __name__=='__main__':
	build_plot(file, months_range)