import pandas as pd

df = pd.read_csv(
    "edu_bigdata_imp1.csv",
    encoding="big5",
    low_memory=False,
)

##開始時間
df_filtered_start = df[df["PseudoID"] == 71]
df_filtered_start = df_filtered_start.dropna(subset=["dp001_review_start_time"])
s_start = pd.Series(pd.to_datetime(df_filtered_start["dp001_review_start_time"]))
dates_start = s_start.dt.date
dates_start = s_start.dt.strftime("%Y-%m-%d")
dates_start = dates_start.dropna()
unique_values_start = dates_start.unique()

##結束時間
df_filtered_end = df[df["PseudoID"] == 71]
df_filtered_end = df_filtered_end.dropna(subset=["dp001_review_end_time"])
s_end = pd.Series(pd.to_datetime(df_filtered_end["dp001_review_end_time"]))
dates_end = s_end.dt.date
dates_end = s_end.dt.strftime("%Y-%m-%d")
dates_end = dates_end.dropna()
unique_values_end = dates_end.unique()

##所有不重複日期
intersection = list(set(unique_values_start) & set(unique_values_end))
print("日期：", intersection)
