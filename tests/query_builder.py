#%%
import pandas as pd
import random 

#%%
RATINGS_PATH = "../data/processed/title.ratings.tsv"

#%%
ratings_df = pd.read_csv(RATINGS_PATH, sep='\t', quotechar='"')
movie_ids = ratings_df["tconst"]
weights = ratings_df["prob"]

#%%
sampled_movie_ids = random.choices(movie_ids, k=10_000, weights=weights)

#%%
f = open("queries.txt", "a")
for i, sample_movie_id in enumerate(sampled_movie_ids):
    f.write(f"{sample_movie_id}")
    if (i != len(sampled_movie_ids) - 1):
        f.write("\n")

f.close()
