import pandas as pd

def parse_excel(file):
  dataframe1 = pd.read_excel(file)
  return dataframe1