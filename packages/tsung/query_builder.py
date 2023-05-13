#%%
import pandas as pd
import random 

#%%
RATINGS_PATH = "../../data/processed/title.ratings.tsv"

#%%
print("query-builder[title.ratings.tsv]: loading data...")
ratings_df = pd.read_csv(RATINGS_PATH, sep='\t', quotechar='"')
movie_ids = ratings_df["tconst"]
weights = ratings_df["prob"]

#%%
print("query-builder[title.ratings.tsv]: sampling ids...")
sampled_movie_ids = random.choices(movie_ids, k=10_000, weights=weights)

#%%
print("query-builder[title.ratings.tsv]: storing sampled ids...")
sampled_movie_df = pd.DataFrame({ 'id': sampled_movie_ids })
sampled_movie_df.to_csv("queries.csv", index=False, header=False)

