print("輸入陣列:")
word = input()
print("輸入n(位移量):")
n = int(input())
print("密文=", end="")
for i in range(len(word)):
    if ord(word[i]) < (91 - n):
        ans = chr(ord(word[i]) + n)
        print(ans, end="")
    else:
        ans = chr(ord(word[i]) - (26 - n))
        print(ans, end="")
