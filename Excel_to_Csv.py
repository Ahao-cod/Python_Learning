import os
import pandas as pd

# 输入文件夹路径和输出文件夹路径
input_folder = r'F:\Test'
output_folder = r'F:\Test'

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        input_file = os.path.join(input_folder, filename)
        df = pd.read_excel(input_file)
        output_file = os.path.join(output_folder, filename[:-5] + ".csv")
        df.to_csv(output_file, index=False,sep=',')




