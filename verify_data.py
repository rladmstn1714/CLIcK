import os
import json

file_path = "/mnt/sda/juyoung/CLICK/Dataset/Language/Contextual/Contextual_TOPIK_new.json"

with open(file_path, "r", encoding="utf-8") as file:
    data_list = json.load(file)
    
# print(data_list)
print(file_path.split("/")[-1])
print(len(data_list))

ids = []
for data in data_list:
    ids.append(data['id'])


dup = {x for x in ids if ids.count(x) > 1}
print(dup)

assert(len(ids) == len(data_list))
assert(len(ids) == len(set(ids)))