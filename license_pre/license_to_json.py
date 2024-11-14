import os
import json

license_key = ['filename', 'license_body', 'key', 'short_name', 'name', 'category', 'owner', 'homepage_url', 'is_exception', 'spdx_license_key', 'text_urls', 'other_urls', 'standard_notice', 'notes', 'other_spdx_license_keys', 'faq_url', 'ignorable_authors', 'ignorable_copyrights', 'ignorable_holders', 'ignorable_urls', 'ignorable_emails', 'minimum_coverage', 'osi_license_key', 'osi_url', 'is_deprecated:', 'is_generic', 'language',]

def convert_license_to_json(license_file):
    with open(license_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    metadata = {}
    license_body = []
    reading_metadata = False
    current_key = None
    current_value = [] 

    metadata['filename'] = os.path.basename(license_file)
    for line in lines:
        line = line.strip()

        if line == '---':
            if not reading_metadata:  # 遇到第一个 '---'，开始读取元数据
                reading_metadata = True
            else:  # 遇到第二个 '---'，结束读取元数据
                reading_metadata = False
            continue
            
        if reading_metadata:
            if ':' in line:
                if current_key:
                    # 保存前一个键的多行值
                    metadata[current_key] = '\n'.join(current_value)
                key, value = line.split(':', 1)

                if key not in license_key: # 只保留列举的键值
                    current_value.append(line)
                    continue

                current_key = key.strip()
                current_value = [value.strip()]
            else:
                if current_key:
                    current_value.append(line)  # 继续添加多行值
        else:
            license_body.append(line)

    if current_key:  # 保存最后一个键的值
        metadata[current_key] = '\n'.join(current_value)

    metadata['license_body'] = '\n'.join(license_body)

    return metadata

def batch_convert(license_directory):
    count = 0
    output_dir = r'benchmark\license_data\license_json'
    os.makedirs(output_dir, exist_ok = True)
    for filename in os.listdir(license_directory):
        if filename.endswith('.license'):
            license_path = os.path.join(license_directory, filename)
            license_data = convert_license_to_json(license_path)

            output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + '.json')
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(license_data, json_file, ensure_ascii=False, indent=4)
                count += 1
                
            print('\r' + str(count), end='', flush=True)
            print(" succeed!", end='')

if __name__ == "__main__":
    directory = r'F:\Python\PY_vscode\benchmark\license_data\LICENSE'
    batch_convert(directory)
