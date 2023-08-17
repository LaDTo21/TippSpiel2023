import pandas as pd

url = 'https://github.com/LaDTo21/TippSpiel2023/blob/729f3e9b3f3fde423f4042f8a4507aec1e6eb0cf/OOF.csv?raw=true'
df = pd.read_csv(url, index_col=0)

print(df.info)
