filename = 'commits-2.txt'
suffix_pattern = '.java'
AVRO = "AVRO-"
commits = []
avro_id = ''

def check_avro(line):
    ind = line.find(AVRO)

    if ind == 4 or ind == 5:
        L = len(line)
        global avro_id
        avro_id = "AVRO-"
        i = 9 - (4 - ind)

        while (i < L and line[i].isdigit()):
            avro_id += line[i]
            i += 1

def commit_check(c):
    if (len(c) != 3):
        return

    if c[2].endswith(suffix_pattern):
        assert(avro_id)
        # c : [changerate, id]
        commits.append([c[2], avro_id])

with open(filename) as file:
    lines = file.readlines()

    for line in lines:
        check_avro(line)

        if line[0].isdigit():
            commit_check(line.split())

output_file = 'result2-2.csv'
# print(commits)

with open(output_file, 'w') as file:
    file.write('FilePath,AVRO-ID\n')

    for c in commits:
        file.write(c[0] + ',' + c[1] + '\n')
