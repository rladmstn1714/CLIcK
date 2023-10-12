import json
from pathlib import Path

def count_problems_in_json(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data_list = json.load(file)
        
        # Ensure problems have unique ids
        ids = []
        for data in data_list:
            ids.append(data['id'])

        dup = {x for x in ids if ids.count(x) > 1}
        if len(dup) > 0:
            raise Exception(f"Duplicate ids: {dup}")

        return len(data_list)  # Assuming that data is a list of problems

def process_dataset(dataset_path):
    dataset_path = Path(dataset_path)
    
    for category_path in dataset_path.iterdir():
        if category_path.is_dir():
            print(f"Processing category: {category_path.name}")
            
            for subcategory_path in category_path.iterdir():
                if subcategory_path.is_dir():
                    print(f"\tProcessing subcategory: {subcategory_path.name}")
                    subcat_cnt = 0
                    
                    for json_path in subcategory_path.iterdir():
                        if json_path.suffix == '.json':
                            # print(f"\t\t\t\tLoading {json_path.name}")
                            problem_count = count_problems_in_json(json_path)
                            subcat_cnt += problem_count
                            print(f"\t\tNumber of problems in {json_path.name}: {problem_count}")
                    print(f"\t{subcat_cnt} problems in subcategory {subcategory_path.name}")
                print("")

# You can customize the path to your dataset directory here
dataset_directory_path = "./Dataset"
process_dataset(dataset_directory_path)
