# %%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# %%
# ============================
# PROCESS NAME_BASICS
# ============================
print("processor[name.basics.tsv]: loading raw data...")
name_basics_df = pd.read_csv("raw/name.basics.tsv", sep="\t",  quotechar='"')

print("processor[name.basics.tsv]: fixing array data...")
name_basics_df["primaryProfession"] = ('{' + name_basics_df["primaryProfession"] +'}')
name_basics_df["knownForTitles"] = ('{' + name_basics_df["knownForTitles"] +'}')

print("processor[name.basics.tsv]: imputing empty fields...")
name_basics_df["birthYear"]          = name_basics_df["birthYear"].replace("\\N", -1) #should be YYYY format dont know
name_basics_df["deathYear"]          = name_basics_df["deathYear"].replace("\\N", -1) #should be YYYY format dont know
name_basics_df["primaryProfession"]  = name_basics_df["primaryProfession"].replace("{\\N}", "{}")
name_basics_df["primaryProfession"]  = name_basics_df["primaryProfession"].replace("{nan}", "{}")
name_basics_df["knownForTitles"]      = name_basics_df["knownForTitles"].replace("{\\N}", "{}")
name_basics_df["knownForTitles"]      = name_basics_df["knownForTitles"].replace("{nan}", "{}")

print("processor[name.basics.tsv]: storing processed data...")
name_basics_df.to_csv("processed/name.basics.tsv", sep='\t', quotechar='"', index=False)
