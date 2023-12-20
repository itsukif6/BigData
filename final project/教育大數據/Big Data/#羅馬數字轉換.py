dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
try:
    while True:
        print("Please enter a roman numeral: ", end="")
        roman = input()
        ans = []
        for i in range(len(roman) - 1):
            if dict[roman[i]] < dict[roman[i + 1]]:
                ans.append(-dict[roman[i]])
            else:
                ans.append(dict[roman[i]])
        ans.append(dict[roman[-1]])
        num = 0
        for i in ans:
            num += i
        print("Your converted numeral is:", num)
except EOFError:
    pass
