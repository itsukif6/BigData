import pandas as pd

df = pd.read_csv(
    "C:/Users/USER/Desktop/112-巨量資料/edu_bigdata_imp1.csv",
    encoding="big5",
    low_memory=False,
)

# 开始时间
df_filtered_start = df[df["PseudoID"] == 71]
df_filtered_start = df_filtered_start.dropna(subset=["dp001_review_start_time"])

# 结束时间
df_filtered_end = df[df["PseudoID"] == 71]
df_filtered_end = df_filtered_end.dropna(subset=["dp001_review_end_time"])

# 合并两列
dates_start = pd.to_datetime(df_filtered_start["dp001_review_start_time"])
dates_end = pd.to_datetime(df_filtered_end["dp001_review_end_time"])

# 获取日期部分
dates_start = dates_start.dt.date
dates_end = dates_end.dt.date

# 找到两个日期列的并集
unique_values = list(set(dates_start) | set(dates_end))

print(unique_values)
