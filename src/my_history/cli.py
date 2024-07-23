import pandas as pd
import sys


def cnt():

    a = sys.argv[1]
    df = pd.read_parquet("~/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(a)]
    cnt = fdf['cnt'].sum()
    print(cnt)
