import os
import json
from datasets import Dataset

def load_exam(file_path):
    print(f"\n\nSTART OF NEW EXAM: {file_path}\n\n")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data_list = json.load(file)
            
            exam_name = file_path.split(".json")[0].split("/")[-1]

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
                        
                    paragraph = data["paragraph"]
                    question = problem["question"]
                    
                    if exam_name.endswith("KIIP"):
                        paragraph = paragraph.replace("설명", "문제")
                        question = paragraph + "\n" + question
                        paragraph = ""
                    
                    if exam_name.endswith("Kedu"):
                        paragraph = paragraph.replace("설명", "문제")
                        question = paragraph + "\n" + question
                        paragraph = ""
                    
                    if exam_name.endswith("TOPIK"):
                        question = question + "\n" + paragraph
                        paragraph = ""
                    
                    if exam_name.endswith("KHB"):
                        question = question + "\n" + paragraph
                        paragraph = ""
                    
                    
                    flattened_data["id"].append(pid)
                    flattened_data["paragraph"].append(paragraph)
                    flattened_data["question"].append(question)
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


def transform_instance(instance, mode=None):
    
    ret_val = {
        'id': instance['id'],
        'paragraph': instance['paragraph'],
        'question': instance['question'],
        'choices': instance['choices'],
        'answer': instance['answer']
    }
    
    return ret_val


def load_dataset():
    end_flag = False
    exam_dict = {}
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                if file.endswith("_new.json"):
                    continue
                
                if file != "Contextual_CSAT.json":
                    continue
                
                print("Processing: ", file)
                file_path = os.path.join(root, file)
                new_file_path = file_path.replace(".json", "_new_new.json")
                
                exam_name = file.split(".json")[0]
                exam_data = load_exam(file_path)
                
                mode = exam_name.split("_")[-1]
                print(mode)
                
                new_exam_data = exam_data.map(transform_instance, mode)
                new_exam_data.to_json(new_file_path, orient="records", lines=True, indent=4, force_ascii=False)
                
                # with open(new_file_path, "w", encoding="utf-8") as f:
                #     json.dump(new_exam_data.to_dict(), f, ensure_ascii=False, indent=4)
                    
                # exam_dict[exam_name] = exam_data
                print("Loading file:", file)
                end_flag = True
        
    return exam_dict

dataset = load_dataset()