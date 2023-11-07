from datasets import load_dataset, DatasetDict, Dataset
import json
import os

class KoreanDatasetBuilder:
    def __init__(self, dataset_dir):
        self.dataset_dir = dataset_dir

    def load(self):
        dataset_dict = DatasetDict()
        for subdir, dirs, files in os.walk(self.dataset_dir):
            for file in files:
                if file.endswith(".json"):  # Check if the file is a JSON file
                    file_path = os.path.join(subdir, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Assuming each file is a separate dataset without splits
                        dataset_name = os.path.basename(subdir) + '_' + file.replace('.json', '')
                        dataset_dict[dataset_name] = Dataset.from_dict(data)
        return dataset_dict

# Usage
dataset_dir = 'path/to/your/Dataset'  # Replace with the path to your Dataset folder
builder = KoreanDatasetBuilder(dataset_dir)
datasets = builder.load()

# Now, you have a dataset_dict object with your datasets that can be manipulated with the Hugging Face datasets library.
