import os
import hashlib

def get_file_checksum(file_path):
    """Return the MD5 checksum of a file."""
    with open(file_path, 'rb') as file:
        file_hash = hashlib.md5()
        while chunk := file.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

def compare_license_files(file1, file2):
    """Compare two files by their checksum."""
    return get_file_checksum(file1) == get_file_checksum(file2)

# Example usage
file1 = 'Benchmark/license_data/LICENSE/Apache-2.0.txt'
file2 = 'Benchmark/license_data/LICENSE/apache-2-0.txt'

if compare_license_files(file1, file2):
    print("The files are identical.")
else:
    print("The files are different.")
