


import pandas as pd
import numpy as np

def get_table_rows(file_name):

    df = pd.read_csv('./'+file_name+'.csv')
    Blocks=dict()
    List_of_Rows=list()

    for index, row in df.iterrows():
            Blocks[index]=row.as_blocks(copy=True)

    for cursor in range(len(Blocks)):
            List_of_Rows.append(dict(Blocks[cursor]["object"]))

    return List_of_Rows
