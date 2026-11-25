import levels
import csv

map = levels.levels[1]

with open("save.csv", "w", newline="") as csvfile:
	fieldnames = ["map", "saved"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	writer.writerow({"map": map, "saved": "save completed"})


with open("save.csv", newline="") as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		if row["saved"] == "save completed":
			print(row["map"])
		print(row)



with open("save.csv", "w", newline="") as csvfile:
	writer = csv.writer(csvfile)

	writer.writerows(map)


with open("save.csv", newline="") as csvfile:
	reader = csv.reader(csvfile)
	map = []
	for row in reader:
		map.append(row)
		print(row)
	print(map)
