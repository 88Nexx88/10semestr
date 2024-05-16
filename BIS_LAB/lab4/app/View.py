import pandas as pd
def View(df, name):
    df.to_html('answer\\html\\'+name)
    return('answer\\html\\'+name)