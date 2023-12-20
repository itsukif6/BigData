import pandas as pd

df = pd.read_csv(
    "edu_bigdata_imp1.csv",
    encoding="big5",
    low_memory=False,
)

df_dp002 = df[df["PseudoID"] != 0]

counts = df_dp002["dp002_verb_display_zh_TW"].value_counts()

top_3 = counts.index[:3]

print(top_3)
