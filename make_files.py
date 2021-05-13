import os
import uuid
import random

num_files_min = 5
num_files_max = 10

len_file_min = 10
len_file_max = 500



for item in os.listdir():
    if not os.path.isdir(item) or item == '.git':
        continue
    num_files_to_make = random.randint(num_files_min, num_files_max)
    print(f'create {num_files_to_make} files in {item}')
    path = os.path.join(os.curdir, item)
    num_files_already = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))])
    for num in range(num_files_already,num_files_already + num_files_to_make):
        filename = f'file{num}.txt'
        filepath = os.path.join(os.curdir, item, filename)
        print(f'  {filepath}')
        with open(filepath,'w') as fid:
            num_val = random.randint(len_file_min, len_file_max)
            for val in range(num_val):
                fid.write(f'{val}\n')

