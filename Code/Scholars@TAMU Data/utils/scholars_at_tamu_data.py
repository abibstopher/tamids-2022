"""Classes for Scholars@TAMU Data Info
Filename: scholars_at_tamu_data.py  
Project Path: TAMIDS/Code/utils/scholars_at_tamu_data.py  
Created Date: 18 March 2022, 17:14 
"""

import json
import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class ScholarsAtTamuDataInfo:
    path_to_df: str
    columns: pd.DataFrame = pd.DataFrame(
        columns=['name', 'description', 'type', 'completness']
        )



if __name__ == '__main__':
    # df = pd.read_excel("../../../Provided Resources/2022 Student Data Science Competition_TAMIDS/Scholars@TAMU Data/people/people_overview.xlsx", sheet_name = 0)
    pass
    # print(df)