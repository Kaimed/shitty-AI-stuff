from csv import *

#holds the first row -- non data
header = []

#nested list of data lines from csv
input_lines = []

#way to divide the counties by population
quartiles = { 1: [],
              2: [],
              3: [],
              4: []
            }
populations = []

#read csv into matrix
with open('county_crime.csv',newline = '') as c:
    Reader = reader(c)
    counter = 0
    for row in Reader:
        if counter == 0:
            header = row
            counter+=1

        else:
            input_lines.append(row)
            if row[1] == 0:
                input_lines.remove(row)

data_dict = {}
for line in input_lines:
    populations.append(line[1])
    del line[len(line)-1]
    data_dict[line[0]] = line[1:]

for item in data_dict.values():
    if item[0] == 0:
        del item[0]
    print(item)
