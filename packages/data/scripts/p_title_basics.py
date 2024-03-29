# %%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# %%
# ============================
# PROCESS TITLE_BASICS
# ============================
print("processor[title.basics.tsv]: loading raw data...")
title_basics_df = pd.read_csv("raw/title.basics.tsv", sep="\t",  quotechar='"', low_memory=False)

# %%
# Remove empty fields
print("processor[title.basics.tsv]: imputing empty fields...")
title_basics_df["startYear"]        = title_basics_df["startYear"].replace("\\N", -1)
title_basics_df["endYear"]          = title_basics_df["endYear"].replace("\\N", -1)
title_basics_df["runtimeMinutes"]   = title_basics_df["runtimeMinutes"].replace("\\N", -1)
title_basics_df["genres"]           = title_basics_df["genres"].replace("\\N", "<EMPTY>")
title_basics_df["isAdult"]          = title_basics_df["isAdult"].replace("\\N", 0)

# %%
# Some tuples are not processed correctly: tab characters inside originalTitle causes wrong column/data association,
# resulting in fields shifted to left by one positions

print("processor[title.basics.tsv]: fixing shifted tuples...")

wrong_splitted = title_basics_df.loc[title_basics_df["genres"].isna()]

wrong_splitted["genres"]            = wrong_splitted["runtimeMinutes"]
wrong_splitted["runtimeMinutes"]    = wrong_splitted["endYear"]
wrong_splitted["endYear"]           = wrong_splitted["startYear"]
wrong_splitted["startYear"]         = wrong_splitted["isAdult"]
wrong_splitted["isAdult"]           = wrong_splitted["originalTitle"]
wrong_splitted["originalTitle"]     = wrong_splitted["primaryTitle"].apply(lambda x: x.split("\t")[1])
wrong_splitted["primaryTitle"]      = wrong_splitted["primaryTitle"].apply(lambda x: x.split("\t")[0])

for idx, row in wrong_splitted.iterrows():
    df_idx = title_basics_df.loc[title_basics_df["tconst"] == row["tconst"]].index[0]
    title_basics_df.at[df_idx, 'genres']            = row["genres"]
    title_basics_df.at[df_idx, 'runtimeMinutes']    = row["runtimeMinutes"] 
    title_basics_df.at[df_idx, 'endYear']           = row["endYear"]
    title_basics_df.at[df_idx, 'startYear']         = row["startYear"]
    title_basics_df.at[df_idx, 'isAdult']           = row["isAdult"]
    title_basics_df.at[df_idx, 'originalTitle']     = row["originalTitle"]
    title_basics_df.at[df_idx, 'primaryTitle']      = row["primaryTitle"]

# %%
# Store sanitized
print("processor[title.basics.tsv]: storing processed data...")
title_basics_df.to_csv("processed/title.basics.tsv", sep='\t', quotechar='"', index=False)
