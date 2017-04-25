# cull - split a csv file by applying a regex to its columns

import os
import pandas as pd
import shutil

ASSET_PATH = '/home/jgp/rone/assets'
DATA_PATH = '/home/jgp/srproj/data'

asset_files = os.listdir(ASSET_PATH) 
asset_paths = [os.path.join(ASSET_PATH, x) for x in asset_files if x[-3:] == 'csv']
data_files = asset_files
data_paths = [os.path.join(DATA_PATH, x) for x in data_files]


def apply_regex(filepath, regex_list):
    print("Reading: ", filepath)
    df = pd.read_csv(filepath, dtype=object)
    df_keys = df.keys()

    # Ignore columns matching these
    index_list = []

    # Apply regex to keys of the index
    for regex in regex_list:
        df_rx = df.filter(regex=regex)
        index_list.append(df_rx)
        df_keys = df_keys.difference(df_rx.keys())

    # Apply new index to dataframe
    df_minus_rx = df.reindex(columns=df_keys)

    return df_minus_rx

def dump_to_csv(df, csv_path):
    # Dump to csv
    df.to_csv(csv_path)

if __name__ == '__main__':
    regex_list = ['L4', 'RPY', 'CIP', 'NPT4', 'WDRAW', 'NUM4', 'C150', '_INC_', 'TRANS', '_RT']

    for i in range(len(asset_paths)): 
        df = apply_regex(asset_paths[i], regex_list)
        dump_to_csv(df, data_paths[i])

