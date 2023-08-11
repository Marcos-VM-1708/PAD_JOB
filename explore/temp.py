import pandas as pd
from ask_2 import df
from pandas import json_normalize
#------------------------------------------------
bd = df[["reviews", "title"]]

bd = pd.DataFrame.from_dict(bd["reviews"], orient='columns')

print(bd)