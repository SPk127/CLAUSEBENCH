import os
import shutil

def get_license_name(license_path):
    license_names = []
    files = os.listdir(license_path)
    for file in files:
        file_path = os.path.join(license_path, file)
        if os.path.isfile(file_path):
            license_names.append(file)
    return license_names
    
def copy_license(src_path, src_licenses, all_licenses):
    dst_path = 'Benchmark/license_data/LICENSE'
    os.makedirs(dst_path, exist_ok=True)
    copy_num = 0
    
    for license_file in src_licenses:
        license_name, _ = os.path.splitext(license_file)
        license_name_norm = license_name.lower().replace('.', '-')  # Normalize to lowercase
        if license_name_norm in all_licenses:
            continue  # Skip if already copied
        src_file_path = os.path.join(src_path, license_file)
        dst_file_path = os.path.join(dst_path, license_file)
        
        shutil.copy(src_file_path, dst_file_path)  # Copy file using shutil
        all_licenses.append(license_name_norm)  # Add to the list of copied licenses
        copy_num += 1
        
    print(f"{src_path} total: {len(src_licenses)}, copy: {copy_num}")
    

if __name__ == '__main__':
    SCANCODE_path = 'Benchmark/license_data/SCANCODE'
    GITHUB_path = 'Benchmark/license_data/GITHUB'
    OSI_path = 'Benchmark/license_data/OSI'
    SPDX_path = 'Benchmark/license_data/SPDX'
    
    SCANCODE_licenses = get_license_name(SCANCODE_path)
    GITHUB_licenses = get_license_name(GITHUB_path)
    OSI_licenses = get_license_name(OSI_path)
    SPDX_licenses = get_license_name(SPDX_path)
    
    all_licenses = []  # To store unique license names
    
    copy_license(SCANCODE_path, SCANCODE_licenses, all_licenses)
    copy_license(SPDX_path, SPDX_licenses, all_licenses)
    copy_license(OSI_path, OSI_licenses, all_licenses)
    copy_license(GITHUB_path, GITHUB_licenses, all_licenses)
