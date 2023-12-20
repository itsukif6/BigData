print("輸入身分證前9碼:")
id = input()
letter = ord(id[0]) - 56
num = (letter // 10) + (letter % 10 * 9)
for i in range(8):
    num += int(id[i + 1]) * (8 - i)
num %= 10
print("完證的身分證字號: ", end="")
print(id, end="")
print(10 - num)
