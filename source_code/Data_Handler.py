

import pandas as pd
import numpy as np
import os



def get_table_rows(file_name):
    """the function return list of dicts , by extracting the tables"""

    path_to_data=os.getcwd().split("/")
    path_to_data[len(path_to_here)-1]="data_sources/"
    path_to_data="/".join(path_to_here)

    df = pd.read_csv(path_to_data+file_name+'.csv')
    Blocks=dict()
    List_of_Rows=list()

    for index, row in df.iterrows():
            Blocks[index]=row.as_blocks(copy=True)

    for cursor in range(len(Blocks)):
            List_of_Rows.append(dict(Blocks[cursor]["object"]))

    return List_of_Rows
