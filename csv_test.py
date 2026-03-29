import pandas as pd

df = pd.read_csv('./exemplo.csv')

df_filtered = df[df['estado'].str.lower() == 'sp']
print(df_filtered)