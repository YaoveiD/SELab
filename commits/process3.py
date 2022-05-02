import csv

bugs = set()
input_file = 'bugfiles-2.csv'

with open(input_file) as f:
    reader = csv.reader(f, delimiter=',')
    total = -1

    for row  in reader:
        total += 1

with open(input_file) as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0

    for row in reader:
        if line_count != 0:
            if line_count * 5 <= total:
                bugs.add(row[0])

        line_count += 1

input_file = 'result1-2.csv'
res = []

with open(input_file) as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0
    
    for row in reader:
        if line_count != 0:
            res.append(row + ["bug-prone" if row[0] in bugs else "non-bug-prone"])

        line_count += 1

output_file = 'result3-2.csv'

with open(output_file, 'w') as f:
    writer = csv.writer(f, delimiter=',')
    f.write('FilePath, ChangeRate, AddLines, DeleteLines, class\n')

    for row in res:
        writer.writerow(row)
