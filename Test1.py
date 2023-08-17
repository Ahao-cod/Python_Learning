import pandas as pd

df = pd.read_excel('your_excel_file.xlsx')

df['指定列名'] = df['指定列名'].fillna('填充值')

df.to_excel('your_updated_excel_file.xlsx', index=False)
