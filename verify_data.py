import os
import json

file_path = "./CLICK/Dataset/Language/Grammar/Grammar_TOPIK_new.json"
# new_file_path = "/mnt/sda/juyoung/CLICK/Dataset/Language/Contextual/Contextual_TOPIK_new_new.json"

with open(file_path, "r", encoding="utf-8") as file:
    data_list = json.load(file)
    
    
# for data in data_list:
    
#     context = data['question'].split("\n")[-1]
#     if len(context) > 50:
#         print(f"paragraph should be {context}, not {data['paragraph']}")
#         data['paragraph'] = context.strip()
#         data['question'] = data['question'].split("\n")[0].strip()
    

# # Open a file for writing with UTF-8 encoding
# with open(new_file_path, 'w', encoding='utf-8') as file:
#     # Iterate through each dictionary in the list
#     for dictionary in data_list:
#         # Convert the dictionary to a JSON string
#         json_str = json.dumps(dictionary, ensure_ascii=False, indent=4)
        
#         # Write the JSON string to the file with a newline
#         file.write(json_str + '\n')
    

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