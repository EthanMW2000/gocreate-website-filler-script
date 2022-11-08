import pandas as pd

def parse_excel(file):
  dataframe1 = pd.read_excel(file)
  dataframe2 = dataframe1.astype('string')
  return dataframe2