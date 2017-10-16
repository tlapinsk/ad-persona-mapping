"""
PARSE BY LOCATION

The next section of code will parse a CSV file pulled from AD to sort security groups by location(department)

Requirements:
  1. You will need a CSV file formatted with the following header: 
  	- title, department, physicaldeliveryoffice, memberof
  2. Ensure memberof values use ';' as a delimiter
"""
import csv
import pprint
from operator import itemgetter
from collections import Counter
from collections import defaultdict

# Read CSV file and parse ALL groups
groups = []
with open('canning.csv') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	for row in reader:
		csv_groups = row[4].split(";")
		for i in csv_groups:
			groups.append(i)

location_group1 = []
location_group2 = []
location_group3 = []
with open('canning.csv') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	for row in reader:
		if row[3] == 'Location1':
			csv_groups = row[4].split(";")
			for i in csv_groups:
				location_group1.append(i)
		elif row[3] == 'Location2':
			csv_groups = row[4].split(";")
			for i in csv_groups:
				location_group2.append(i)
		elif row[3] == 'Location3a or Location3b':
			csv_groups = row[4].split(";")
			for i in csv_groups:
				location_group3.append(i)

# Count groups in each location
count = []
for i in groups:
  x = groups.count(i)
  count.append([i,x])

count_location1 = []
for i in location_group1:
  x = location_group1.count(i)
  count_location1.append([i,x])

count_location2 = []
for i in location_group2:
  x = location_group2.count(i)
  count_location2.append([i,x])

count_location3 = []
for i in location_group3:
	x = location_group3.count(i)
	count_location3.append([i,x])

# Get rid of duplicates
new_count = []
for i in count:
	if i not in new_count:
		new_count.append(i)

new_count_location1 = []
for i in count_location1:
	if i not in new_count_location1:
		new_count_location1.append(i)

new_count_location2 = []
for i in count_location2:
	if i not in new_count_location2:
		new_count_location2.append(i)

new_count_location3 = []
for i in count_location3:
	if i not in new_count_location3:
		new_count_location3.append(i)

# Sort from highest to lowest number
sort = sorted(new_count, key=itemgetter(1), reverse=True)
sort_location1 = sorted(new_count_location1, key=itemgetter(1), reverse=True)
sort_location2 = sorted(new_count_location2, key=itemgetter(1), reverse=True)
sort_location3 = sorted(new_count_location3, key=itemgetter(1), reverse=True)
print()
print(sort)
print()
print(sort_location1)
print()
print(sort_location2)
print()
print(sort_location3)

# Write to CSV
Locations = [['ALL'], ['LOCATION1'], ['LOCATION2'], ['LOCATION3']]
with open('location.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(Locations[0])
    writer.writerows(sort)
    writer.writerows(Locations[1])
    writer.writerows(sort_location1)
    writer.writerows(Locations[2])
    writer.writerows(sort_location2)
    writer.writerows(Locations[3])
    writer.writerows(sort_location3)

"""
PARSE BY JOB DESCRIPTION

The next section of code will parse a CSV file pulled from AD to sort security groups by job title

Requirements:
  1. You will need a CSV file formatted with the following header: 
  	- title, department, physicaldeliveryoffice, memberof
  2. Ensure memberof values use ';' as a delimiter
"""

# Parse job descriptions
# Create dictionary of jobs and associated values
jobs = {}
with open('canning.csv', mode='rU') as f:
    reader = csv.reader(f, delimiter=',')  # dialect=csv.excel_tab?
    for n, row in enumerate(reader):
        if not n:
            # Skip header row (n = 0).
            continue  
        name, title, department, office, group = row
        if title not in jobs:
            jobs[title] = list()
        jobs[title].append((group.split(';')))

# Combined nested lists for each dictionary key
for k, v in jobs.items():
	temp = []
	for i in v:
		if isinstance(i,list):
			temp.extend(i)
		else:
			temp.append(i)
	jobs[k]=temp
# pprint.pprint(jobs)

# Count and sort group values
for k, v in jobs.items():
	for i in v:
		temp = []
		x = (Counter(v))
		x = sorted(x.items(), key=lambda pair: pair[1], reverse=True)
		temp.append(x)
	jobs[k]=temp

# Convert dictionary to list of tuples
convert_list = [(k, *t) for k, v in jobs.items() for t in v[0]]
print()
pprint.pprint(convert_list)

# Write to CSV
with open('job_title.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(convert_list)