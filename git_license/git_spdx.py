import requests
import json
import os

# 下载SPDX许可证列表
spdx_url = "https://spdx.org/licenses/licenses.json"
response = requests.get(spdx_url)
licenses = response.json()
num = 0

if os.path.exists("/home/keqiang/Benchmark/license_data/SPDX") is False:
    os.mkdir("/home/keqiang/Benchmark/license_data/SPDX")

# 批量下载每个许可证的文本
for license_data in licenses['licenses']:
    license_id = license_data['licenseId']
    license_url = f"https://spdx.org/licenses/{license_id}.json"
    license_text = requests.get(license_url).json()
    
    # 将许可证文本保存为本地文件
    if os.path.exists(f"/home/keqiang/Benchmark/license_data/SPDX/{license_id}.txt"):
        continue
    
    with open(f"/home/keqiang/Benchmark/license_data/SPDX/{license_id}.txt", "w", encoding="utf-8") as f:
        f.write(license_text["licenseText"])
    print(f"Downloaded {license_id}")
    num += 1
    
print(f"Downloaded {num} license")

