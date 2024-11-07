import os

folder_path = r'F:\Python\PY_vscode\benchmark\license_data\LICENSE'

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        name, ext = os.path.splitext(filename)
        new_file_path = os.path.join(folder_path, name + '.license')
        os.rename(file_path, new_file_path)
        print(f"Renamed: {file_path} -> {new_file_path}")

print("All files have been renamed.")
