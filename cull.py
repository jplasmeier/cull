# cull - split a csv file by applying a regex to its columns

import pandas as pd

df = pd.read_csv('college_scorecard.csv', dtype=object)
df_keys = df.keys()

# Ignore columns matching these
regex_list = ['L4', 'RPY', 'CIP', 'NPT4', 'WDRAW', 'NUM4', 'C150', '_INC_', 'TRANS', '_RT']
index_list = []

# Apply regex to keys of the index
for regex in regex_list:
    df_rx = df.filter(regex=regex)
    index_list.append(df_rx)
    df_keys = df_keys.difference(df_rx.keys())

# Apply new index to dataframe
df_minus_rx = df.reindex(columns=df_keys)

# Dump to csv
df_minus_rx.to_csv('college_scorecard_less.csv')

