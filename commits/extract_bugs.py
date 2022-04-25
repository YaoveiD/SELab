import csv
input_file = 'bugs.csv'
keys = set()

with open(input_file) as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0

    for row in reader:
        if line_count != 0:
            keys.add(row[1])

        line_count += 1

input_file = 'result2-2.csv'
bug_count = dict()

with open(input_file) as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0

    for row in reader:
        if line_count != 0 and row[1] in keys:
            if row[0] not in bug_count:
                bug_count[row[0]] = 0

            bug_count[row[0]] += 1

        line_count += 1

res = []

for bug, count in bug_count.items():
    res.append((bug, count))

res.sort(key = lambda x: x[1])
res.reverse()

output_file = 'bugfiles-2.csv'

with open(output_file, 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['FilePath', 'BugRate'])

    for row in res:
        writer.writerow(row)