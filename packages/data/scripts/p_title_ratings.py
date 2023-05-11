# %%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
print(f'pandas v.{pd.__version__}')
# %%

# %%
# ============================
# PROCESS TITLE_RATINGS
# ============================
print("processor[title.ratings.tsv]: loading raw data...")
title_ratings_df = pd.read_csv("raw/title.ratings.tsv", sep="\t",  quotechar='"')


#%%
print("processor[title.ratings.tsv]: assigning probabilities...")

title_ratings_sum        = title_ratings_df["numVotes"].sum()
title_ratings_df["prob"] = 0.0
title_ratings_df["prob"] = title_ratings_df["numVotes"] / title_ratings_sum
title_ratings_df.head()

# %%
# No sanitization required -> store
print("processor[title.ratings.tsv]: storing processed data...")
title_ratings_df.to_csv("processed/title.ratings.tsv", sep='\t', quotechar='"', index=False)
