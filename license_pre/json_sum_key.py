import json
import os
from collections import defaultdict

if __name__ == "__main__":
    json_dir = r'/home/keqiang/Benchmark/license_data/license_json'
    json_files = os.listdir(json_dir)
    
    key_count = defaultdict(int)
    
    for json_file in json_files:
        json_path = os.path.join(json_dir, json_file)
        
        with open(json_path, 'r',  encoding='utf-8') as f:
            data = json.load(f)
            
        #count_flag = False
        # for key, value in data.items():
        #     key_count[key] += 1
        #     if value == [] or value is None:
        #         print(json_path)
        
        for key, value in data.items():
            if key == 'category':
                key_count[value] += 1
        
    for key, count in key_count.items():
        print(f"{key}: {count}")
