import time
from urllib.request import urlopen
from urllib.request import Request
import urllib.error
import json

def get_last_recorded_repo(file_path):
    """从文件中读取最后一行的仓库数据"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                count = len(lines)
                last_line = lines[-1].strip()
                repo_data = last_line.split(',')
                url = 'https://api.github.com/search/repositories?q={full_name}'.format(full_name=repo_data[1])
                req = Request(url)
                response = urlopen(req).read()
                result = json.loads(response.decode())
                min_stars = result['items'][0]['stargazers_count']
                search = f'stars:<{min_stars}'
                return count, search
            else:
                return 0, None # 初始状态
    except FileNotFoundError:
        return 0, None  # 文件不存在时从初始状态开始
    
count , search = get_last_recorded_repo('/home/keqiang/Benchmark/license_data/Repos.txt')
print(count)
print(search)