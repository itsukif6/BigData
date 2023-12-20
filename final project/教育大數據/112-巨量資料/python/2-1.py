import pandas as pd

df = pd.read_csv(
    "edu_bigdata_imp1.csv",
    encoding="big5",
    low_memory=False,
)

df_filtered = df[df["PseudoID"] == 281]

df_filtered = df_filtered.dropna(subset=["dp001_indicator"])

df_unique = df_filtered.drop_duplicates(subset="dp001_video_item_sn")

print(df_unique[["dp001_video_item_sn", "dp001_indicator"]])
