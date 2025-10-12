import os
import shutil

lbp_path = r"C:\Lbp"

folders = ["Basics", "Conditions", "Loops", "Patterns"]

# Create folders if not exist
for folder in folders:
    os.makedirs(os.path.join(lbp_path, folder), exist_ok=True)

# Go through files
for file in os.listdir(lbp_path):
    file_path = os.path.join(lbp_path, file)
    
    if os.path.isdir(file_path):
        continue
    
    # Try automatic first (optional, can skip)
    auto_moved = False
    keywords = {
        "Basics": ["hello", "greet", "vowels", "string"],
        "Conditions": ["if", "elif", "nestedif", "armstrong", "leap", "grade", "prime", "power", "withdrawl"],
        "Loops": ["for", "while", "factorial", "fibonacci", "num", "sum", "div", "even", "odd", "table", "reversenum", "mul"],
        "Patterns": ["pattern", "pyramid", "triangle", "stars", "col", "row", "inv"]
    }
    
    for folder, keys in keywords.items():
        if any(k.lower() in file.lower() for k in keys):
            shutil.move(file_path, os.path.join(lbp_path, folder, file))
            auto_moved = True
            print(f"Moved {file} → {folder} (auto)")
            break
    
    # If skipped, ask user
    if not auto_moved:
        print(f"\nFile: {file}")
        print("Choose folder to move to:")
        for i, folder in enumerate(folders, 1):
            print(f"{i}. {folder}")
        print("0. Skip / Leave here")
        choice = input("Enter number: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(folders):
                shutil.move(file_path, os.path.join(lbp_path, folders[choice-1], file))
                print(f"Moved {file} → {folders[choice-1]}")
            else:
                print(f"Skipped {file}")
        else:
            print(f"Skipped {file}")
3