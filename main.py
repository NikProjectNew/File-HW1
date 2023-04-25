from pprint import pprint
import os

files = ['1.txt', '2.txt', '3.txt']

file_data = []

for file in files:
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
        file_data.append((file, len(lines), lines))

sorted_file_data = sorted(file_data, key=lambda data: data[1])


pprint(sorted_file_data,  sort_dicts=False)