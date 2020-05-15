import os
import sys

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

print("Scanning directories size for :", path, '\n')


def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


output = []
for dir in os.listdir(path):
    full_path_dir = os.path.join(path, dir)
    if os.path.isdir(full_path_dir):
        size = round(get_size(full_path_dir)/1000000)
        out = [dir, ' ', size, 'MB']
        output += [out]

output.sort(key = lambda x: x[2])
output.reverse()

max_dir_len = 0
for line in output:
    l = len(line[0])
    if l > max_dir_len:
        max_dir_len = l

for index, line in enumerate(output):
    dir_len = len(line[0])
    delta = max_dir_len - dir_len
    line[1] = '-' * delta
    line[2] = str(line[2])
    output[index] = ' '.join(line)


output = '\n'.join(output)
print(output)
