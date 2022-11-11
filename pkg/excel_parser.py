import pandas as pd

def parse_excel(file: str) -> pd.DataFrame:
  raw_dataframe = pd.read_excel(file)
  df_string = raw_dataframe.astype('string')
  return df_string