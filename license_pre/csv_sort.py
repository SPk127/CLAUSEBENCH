import pandas as pd

# 读取 CSV 文件
input_file = r'F:\Python\PY_vscode\benchmark\license_data\license_scan\SPDX2CSV_LICENSE.zip.csv'
output_file = r'F:\Python\PY_vscode\benchmark\license_data\license_scan\LICENSE_SPDX2CSV.csv'

# 加载 CSV 数据
data = pd.read_csv(input_file)

# 按 FileName 列字母序排序
sorted_data = data.sort_values(by='FileName')

# 将排序后的数据写入新的 CSV 文件
sorted_data.to_csv(output_file, index=False)

print(f"已将数据按 FileName 排序并保存到 {output_file}")