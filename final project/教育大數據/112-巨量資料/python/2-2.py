import pandas as pd

df = pd.read_csv(
    "edu_bigdata_imp1.csv",
    encoding="big5",
    low_memory=False,
)

df_filtered = df[(df["PseudoID"] == 281) & (df["dp001_prac_score_rate"] == 100)]

df_filtered = df_filtered.dropna(subset=["dp001_prac_date"])

df_unique = df_filtered.drop_duplicates(subset="dp001_prac_score_rate")

print(len(df_filtered))
