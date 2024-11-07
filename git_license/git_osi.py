import requests
from bs4 import BeautifulSoup
import os

path = "/home/keqiang/Benchmark/license_data/OSI"

# OSI 许可证列表页面
for i in range(1, 11):
    osi_url = f"https://opensource.org/license/page/{i}"
    response = requests.get(osi_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # 查找所有许可证的链接
    license_links = soup.find_all('a', href=True)

    for link in license_links:
        license_url = link['href']
        if license_url.startswith("https://opensource.org/license") and license_url.split("/")[-2] == "license":
            # full_url = f"https://opensource.org{license_url}"
            license_page = requests.get(license_url)
            license_soup = BeautifulSoup(license_page.content, 'html.parser')
            # 提取许可证文本
            license_div = license_soup.find('div', {'class': 'entry-content post--content license-content'})
            if license_div:
                # 获取 div 中所有的文本内容
                license_text = license_div.get_text(separator='\n', strip=True)
                # 生成文件名（可以根据URL或其他规则生成）
                license_name = license_url.split('/')[-1] + ".txt"
                
                if os.path.exists(os.path.join(path, license_name)):
                    continue
                with open(os.path.join(path, license_name), 'w', encoding='utf-8') as f:
                    f.write(license_text)
                print(f"License found {license_name}")

            else:
                print(f"License text not found for {license_url}")
