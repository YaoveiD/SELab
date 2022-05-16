# created: May 16 22 07:14 PM
import csv

input_file = 'avro-1.9.0.csv'
suffix_pattern = '.java'
cyclomatic = dict() # key : file_name, value : cyclomatic
save = [] # list of tuples: [(class or method, cyclomatic), ...]

with open(input_file) as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0

    for row in reader:
        if line_count != 0:
            if row[0] == 'File' and row[1].endswith(suffix_pattern): # .java file
                cyclomatic[row[1]] = 0
            elif row[2] != '':
                save.append((row[1], int(row[2])))

        line_count += 1

matches = 0

for stuff, c in save:
    fixed_name = '/'.join(stuff.split('.')[:-1]) + suffix_pattern

    # I don't know, just a fast way to implement
    for name in cyclomatic:
        if name.endswith(fixed_name):
            cyclomatic[name] += 1
            matches += 1

print(len(cyclomatic), matches)

bugs = set()
input_file = 'bugfiles.csv'

with open(input_file) as f:
    reader = csv.reader(f, delimiter=',')
    total = -1

    for row in reader:
        total += 1

with open(input_file) as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0

    for row in reader:
        if line_count != 0:
            if line_count * 5 <= total:
                bugs.add(row[0])

        line_count += 1

output_file = 'result.csv'
prefix = 'lang/java/'

with open(output_file, 'w') as f:
    writer = csv.writer(f, delimiter=',')
    f.write('FilePath, Cyclomatic, Class\n')

    for name, c in cyclomatic.items():
        fixed_name = prefix + name
        row = [fixed_name, c, 'bug-prone' if fixed_name in bugs else 'not-bug-prone']
        writer.writerow(row)
