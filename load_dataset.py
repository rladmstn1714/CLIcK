import os
import json
from datasets import Dataset

def load_exam(file_path):
    print(f"\n\nSTART OF NEW EXAM: {file_path}\n\n")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data_list = json.load(file)

            # Flatten the data structure
            flattened_data = {
                "id": [],
                "paragraph": [],
                "question": [],
                "choices": [],
                "answer": [],
            }

            for data in data_list:
                for problem in data["problems"]:
                    if "idx" in problem:
                        pid = f"{data['id']}_{problem['idx']}"
                    else:
                        pid = f"{data['id']}"

                    flattened_data["id"].append(pid)
                    flattened_data["paragraph"].append(data["paragraph"])
                    flattened_data["question"].append(problem["question"])
                    flattened_data["choices"].append(problem["choices"])
                    flattened_data["answer"].append(problem["answer"])
                    
                    print("")
                    print("==" * 40)
                    print(pid)
                    print(f"paragraph:\n{data['paragraph']}")
                    print(f"question:\n{problem['question']}")
                    choices_str = "\n".join(problem["choices"])
                    print(f"choices:\n{choices_str}")
                    print(f"\nanswer: \n{problem['answer']}")

            # Convert the flattened data to HuggingFace Dataset format
            dataset = Dataset.from_dict(flattened_data)
            return dataset
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return None

def load_dataset():
    exam_dict = {}
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                
                if "KIIP" in file_path:
                    continue
                
                exam_name = file.split(".json")[0]
                exam_data = load_exam(file_path)
                exam_dict[exam_name] = exam_data
                
                
    return exam_dict

dataset = load_dataset()