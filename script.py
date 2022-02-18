import os
import csv

l = os.listdir('dataset/')

with open('dataset.csv', 'w') as file:
	csv_writer = csv.writer(file)
	for path in l:
		label = path.split('_')
		
		if not label[0].isnumeric():
			label = label[0][0] + label[2][0]
		else:
			label = label[0] + label[2][0]

		csv_writer.writerow(['TRAINING', path, label, 0, 0, 1, 1])