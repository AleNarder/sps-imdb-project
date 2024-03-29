# %%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# %%
# ============================
# PROCESS TITLE_PRINCIPALS
# ============================

print("processor[title.principals.tsv]: loading raw data by chuncks...")
title_principals_df=None

for chunk in pd.read_csv("raw/title.principals.tsv", sep="\t",  quotechar='"' , chunksize=100000):
    chunk["category"]  = chunk["category"].replace("\\N", "<EMPTY>")
    chunk["job"]  = chunk["job"].replace("\\N", "<EMPTY>")
    chunk["characters"]  = chunk["characters"].replace("\\N", "<EMPTY>")
    chunk["ordering"]  = chunk["ordering"].replace("\\N", -1)

    title_principals_df=pd.concat([title_principals_df,chunk])

print("processor[title.principals.tsv]: storing processed data...")
title_principals_df.to_csv("processed/title.principals.tsv", sep='\t', quotechar='"', index=False)


