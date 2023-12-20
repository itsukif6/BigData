import pandas as pd

df = pd.read_csv(
    "edu_bigdata_imp1.csv",
    encoding="big5",
    low_memory=False,
)

df_filtered = df[df["PseudoID"] == 39]

unique_values = df_filtered["dp001_review_sn"].unique()

print(len(unique_values))
