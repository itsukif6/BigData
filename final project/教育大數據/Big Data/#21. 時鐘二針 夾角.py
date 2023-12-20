print("時:", end="")
hour = int(input())
print("分:", end="")
minute = int(input())
minute_angel = minute * 6
hour_angel = 30 * hour + 0.5 * minute
print("分的角度:", minute_angel)
print("時的角度:", hour_angel)
print("相差", abs(hour_angel - minute_angel))
