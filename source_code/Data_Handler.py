


import pandas as pd
import numpy as np
import os
import json
import sys

vague_for_computer=["false","False","F","f"]

if len(sys.argv)>1:
    if sys.argv[1] in vague_for_computer:
        write_on_file=not(bool(sys.argv[1]))
    else :
        write_on_file=bool(sys.argv[1])


def write_json(json_structure):
    if write_on_file:
        f=open(file_name+'.json', 'w+')
        f.write(str(json_structure))
        f.close()

def get_table_rows(file_name,type_of_data):
    """the function return list of dicts , by extracting the tables"""

    path_to_data=os.getcwd().split("/")
    path_to_data[len(path_to_data)-1]="data_sources/"
    path_to_data="/".join(path_to_data)

    df = pd.read_csv(path_to_data+file_name+'.csv')

    if "table" in type_of_data:
        return df

    Blocks=dict()
    List_of_Rows=list()

    for index, row in df.iterrows():
            Blocks[index]=row.as_blocks(copy=True)

    for cursor in range(len(Blocks)):
            List_of_Rows.append(dict(Blocks[cursor]["object"]))

    return List_of_Rows




if len(sys.argv)>1:
    file_name=sys.argv[2] # provide name without externsion of the file like trucks
    json_structure=json.dumps(get_table_rows(file_name))
    write_json(json_structure)
