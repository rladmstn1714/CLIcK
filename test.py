import os

# Define the root directory of your dataset
root_dir = "."

# Walk through all subdirectories in the root directory
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # Check if the file ends with '_new.json'
        if file.endswith("_new.json"):
            old_file_path = os.path.join(subdir, file)
            # Create the new file name by replacing '_new.json' with '.json'
            new_file_path = os.path.join(subdir, file.replace("_new.json", ".json"))
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{old_file_path}' to '{new_file_path}'")
