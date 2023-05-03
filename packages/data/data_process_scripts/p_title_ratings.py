# %%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
print(f'pandas v.{pd.__version__}')
import gc
# %%

# %%
# ============================
# PROCESS TITLE_RATINGS
# ============================
print("processor[title.ratings.tsv]: loading raw data...")
title_ratings_df = pd.read_csv("raw/title.ratings.tsv", sep="\t",  quotechar='"')


#%%
print("processor[title.ratings.tsv]: assigning probabilities...")

title_ratings_df["prob"] = [0.0 for i in range (0, len(title_ratings_df.index), 1)]

title_ratings_sum = 0

for rating in title_ratings_df["averageRating"]:
    title_ratings_sum += rating

title_ratings_df["prob"] = title_ratings_df["averageRating"].apply(lambda x: x / title_ratings_sum )

# %%
# No sanitization required -> store
print("processor[title.ratings.tsv]: storing processed data...")
title_ratings_df.to_csv("processed/title.ratings.tsv", sep='\t', quotechar='"', index=False)
