# %%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
#print(f'pandas v.{pd.__version__}')
import gc
# %%

# %%
# ============================
# PROCESS TITLE_EPISODE
# ============================
print("processor[title.episode.tsv]: loading raw data...")
title_episode_df = pd.read_csv("raw/title.episode.tsv", sep="\t",  quotechar='"')

print("processor[title.episode.tsv]: imputing empty fields...")
title_episode_df["seasonNumber"]  = title_episode_df["seasonNumber"].replace("\\N", -1)
title_episode_df["episodeNumber"] = title_episode_df["episodeNumber"].replace("\\N", -1)



print("processor[title.episode.tsv]: storing processed data...")
title_episode_df.to_csv("processed/title.episode.tsv", sep='\t', quotechar='"', index=False)
