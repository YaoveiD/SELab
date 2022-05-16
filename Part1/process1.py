filename = 'commits-2.txt'
suffix_pattern = '.java'
commits = dict()

def commit_check(c):
    if (len(c) != 3):
        return

    if c[2].endswith(suffix_pattern):
        # c : [changerate, addlines, deletelines, id]
        if c[2] not in commits:
            commits[c[2]] = [0, 0, 0]

        commits[c[2]][0] += 1
        commits[c[2]][1] += int(c[0])
        commits[c[2]][2] += int(c[1])

with open(filename) as file:
    lines = file.readlines()

    for line in lines:
        if line[0].isdigit():
            commit_check(line.split())

output_file = 'result-2.csv'

with open(output_file, 'w') as file:
    file.write('FilePath, ChangeRate, AddLines, DeleteLines\n')

    for path, changes in commits.items():
        file.write(path + ',' + str(changes[0]) + ',' + str(changes[1]) + ',' + str(changes[2]) + '\n')