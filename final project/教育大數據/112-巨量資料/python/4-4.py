import pandas as pd

df = pd.read_csv(
    "edu_bigdata_imp1.csv",
    encoding="big5",
    low_memory=False,
)

df_dp002 = df[df["dp002_extensions_alignment"] == '["校園職業安全"]']
data_count = df_dp002["dp002_extensions_alignment"].value_counts().max()

print(data_count)
