# %%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
#print(f'pandas v.{pd.__version__}')
# %%

# %%
# ============================
# PROCESS TITLE_CREW
# ============================
print("processor[title.crew.tsv]: loading raw data...")
title_crew_df = pd.read_csv("raw/title.crew.tsv", sep="\t",  quotechar='"')

print("processor[title.crew.tsv]: fixing array data...")

temp=[]
for i in title_crew_df["directors"]:
    temp.append('{' + i +'}')
title_crew_df["directors"]=temp

temp=[]
for i in title_crew_df["writers"]:
    temp.append('{' + i +'}')
title_crew_df["writers"]=temp

title_crew_df["writers"]           = title_crew_df["writers"].replace("{\\N}", "{}")
title_crew_df["directors"]         = title_crew_df["directors"].replace("{\\N}", "{}")

print("processor[title.crew.tsv]: storing processed data...")
title_crew_df.to_csv("processed/title.crew.tsv", sep='\t', quotechar='"', index=False)

