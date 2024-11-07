import os
import re

path = "/home/keqiang/Benchmark/license_data/SPDX"
pattern = re.compile("<head><title>404 Not Found</title></head>")
num = 0

files_name = os.listdir(path)
for file_name in files_name:
    if file_name.endswith(".txt"):
        file_path = os.path.join(path, file_name)
        with open(file_path, "r") as f:
            data = f.read()
            if re.search(pattern, data) != None:
                print("remove: " + file_path.split(".")[0].split("/")[-1])
                os.remove(file_path)
                num += 1
                
print(f"remove {num} successfully")