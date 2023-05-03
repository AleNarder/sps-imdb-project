# %%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
print(f'pandas v.{pd.__version__}')
import gc

# %%


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

del title_basics_df
del wrong_splitted
gc.collect()

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

# %%
# ============================
# PROCESS TITLE_CREW
# ============================
print("processor[title.crew.tsv]: loading raw data...")
title_crew_df = pd.read_csv("raw/title.crew.tsv", sep="\t",  quotechar='"')

temp=[]
for i in title_crew_df["directors"]:
    temp.append('{' + i +'}')
title_crew_df["directors"]=temp

temp=[]
for i in title_crew_df["writers"]:
    temp.append('{' + i +'}')
title_crew_df["writers"]=temp

title_crew_df["writers"]           = title_crew_df["writers"].replace("\\N", "{}")
title_crew_df["directors"]         = title_crew_df["directors"].replace("\\N", "{}")

print("processor[title.crew.tsv]: storing processed data...")
title_crew_df.to_csv("processed/title.crew.tsv", sep='\t', quotechar='"', index=False)


# %%
# ============================
# PROCESS TITLE_EPISODE
# ============================
print("processor[title.episode.tsv]: loading raw data...")
title_episode_df = pd.read_csv("raw/title.episode.tsv", sep="\t",  quotechar='"')

print("processor[title.episode.tsv]: imputing empty fields...")
title_episode_df["seasonNumber"]        = title_episode_df["seasonNumber"].replace("\\N", -1)
title_episode_df["episodeNumber"]        = title_episode_df["episodeNumber"].replace("\\N", -1)



print("processor[title.episode.tsv]: storing processed data...")
title_episode_df.to_csv("processed/title.episode.tsv", sep='\t', quotechar='"', index=False)


# %%
# ============================
# PROCESS NAME_BASICS
# ============================
print("processor[name.basics.tsv]: loading raw data...")
name_basics_df = pd.read_csv("raw/name.basics.tsv", sep="\t",  quotechar='"')

temp=[]
for i in name_basics_df["primaryProfession"]:
    temp.append('{' + str(i) +'}')
name_basics_df["primaryProfession"]=temp
temp=[]
for i in name_basics_df["knownForTitles"]:
    temp.append('{' + str(i) +'}')
name_basics_df["knownForTitles"]=temp

print("processor[name.basics.tsv]: imputing empty fields...")
name_basics_df["birthYear"]          = name_basics_df["birthYear"].replace("\\N", -1) #should be YYYY format dont know
name_basics_df["deathYear"]          = name_basics_df["deathYear"].replace("\\N", -1) #should be YYYY format dont know
name_basics_df["primaryProfession"]  = name_basics_df["primaryProfession"].replace("\\N", "<EMPTY>")
name_basics_df["knownForTitles"]      = name_basics_df["knownForTitles"].replace("\\N", "<EMPTY>")




print("processor[name.basics.tsv]: storing processed data...")
name_basics_df.to_csv("processed/name.basics.tsv", sep='\t', quotechar='"', index=False)

del title_crew_df
del title_ratings_df
del title_episode_df
del name_basics_df
del temp
gc.collect()

# %%
# ============================
# PROCESS TITLE_PRINCIPALS
# ============================

print("processor[title.principals.tsv]: loading raw data...")
title_principals_df=None
for chunk in pd.read_csv("raw/title.principals.tsv", sep="\t",  quotechar='"' , chunksize=1000000):
    chunk["category"]  = chunk["category"].replace("\\N", "<EMPTY>")
    chunk["job"]  = chunk["job"].replace("\\N", "<EMPTY>")
    chunk["characters"]  = chunk["characters"].replace("\\N", "<EMPTY>")
    chunk["ordering"]  = chunk["ordering"].replace("\\N", -1)
    title_principals_df=pd.concat([title_principals_df,chunk])

#title_principals_df = pd.read_csv("raw/title.principals.tsv", sep="\t",  quotechar='"' , low_memory=False)

print("processor[title.principals.tsv]: storing processed data...")
title_principals_df.to_csv("processed/title.principals.tsv", sep='\t', quotechar='"', index=False)


