def arabic_to_chinese(amount):
    chinese_numerals = {
        0: "零",
        1: "壹",
        2: "貳",
        3: "參",
        4: "肆",
        5: "伍",
        6: "陸",
        7: "柒",
        8: "捌",
        9: "玖",
    }

    unit_positions = ["", "拾", "佰", "仟"]
    decimal_positions = ["", "萬", "億", "兆"]

    amount_str = str(amount)
    len_amount = len(amount_str)

    result = ""
    for i in range(len_amount):
        digit = int(amount_str[i])

        if digit != 0:
            result += chinese_numerals[digit] + unit_positions[(len_amount - i - 1) % 4]
        else:
            if i != len_amount - 1 and int(amount_str[i + 1]) != 0:
                result += chinese_numerals[digit]

        if (len_amount - i - 1) % 4 == 0 and i != len_amount - 1:
            result += decimal_positions[(len_amount - i - 1) // 4]
    ans = list(result.strip())
    for i in range(len(ans) - 1, -1, -1):
        if ans[i] == "兆" or ans[i] == "億" or ans[i] == "萬":
            if ans[i - 1] == "零":
                ans.pop(i - 1)

    ans_list = [str(element) for element in ans]
    result = ""
    result = result.join(ans_list)
    return result + "元"


try:
    while True:
        print("請輸入數字:", end="")
        amount = int(input())
        chinese_amount = arabic_to_chinese(amount)
        print(f"{amount} 的大寫中文表示為：{chinese_amount}")
except EOFError:
    pass
