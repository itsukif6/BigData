import pandas as pd

df = pd.read_csv(
    "edu_bigdata_imp1.csv",
    encoding="big5",
    low_memory=False,
)

df_dp001 = df[df["PseudoID"] != 0]
most_viewed = df_dp001["dp001_review_sn"].value_counts().idxmax()
view_count = df_dp001["dp001_review_sn"].value_counts().max()

print(int(most_viewed), view_count)
