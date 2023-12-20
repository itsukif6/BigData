"""
import requests

res = requests.get(
    "https://ecshweb.pchome.com.tw/search/v3.3/?q=corsair%20void%20elite&scope=all"
)
print(res.text)
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--enable-chrome-browser-cloud-management")
chrome_options.add_argument(
    "webdriver.chrome.driver=.\\final project\\chromedriver.exe"
)
driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://ecshweb.pchome.com.tw/search/v3.3/?q=corsair%20void%20elite&scope=all"
)

# 等待一段時間，讓網頁充分加載
driver.implicitly_wait(10)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# 創建 Datalist
pname = []
pprice = []
phave = []

# 找到所有包含產品信息的區塊
product_blocks = soup.find_all("div", class_="layout-wrapper")

for block in product_blocks:
    # 提取產品名稱
    product_name_tag = block.find_all("h5", class_="prod_name")
    for product_name in product_name_tag:
        # Use .text.strip() to get the stripped text
        name = product_name.text.strip()
        # 將數據添加到 Datalist
        pname.append(name)
        print(name)
    # if product_name_tag:
    #     product_name = product_name_tag.text.strip()

    # else:
    #     product_name = "未找到名稱為 CORSAIR VOID RGB ELITE 的產品"

    # 提取價格
    price = block.find_all("span", class_="price")  # .text.strip()
    for price_uni in price:
        # Use .text.strip() to get the stripped text
        price_unique = price_uni.text.strip()
        # 將數據添加到 Datalist
        pprice.append(price_unique)
        print(price_unique)

    # 是否有貨
    button_tag = block.find_all("button", class_="unblock")
    for button in button_tag:
        # Use .text.strip() to get the stripped text
        button_uni = button.text.strip()
        # 將數據添加到 Datalist
        phave.append(button_uni)
        print(button_uni)


# 將 DataFrame 寫入 Excel 文件
with xlsxwriter.Workbook("product_data.xlsx") as workbook:
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, "產品名稱")
    for i in range(len(pname)):
        print("pname:", pname[i])
        worksheet.write(i + 1, 0, str(pname[i]))

    worksheet.write(0, 1, "價格")
    for i in range(len(pprice)):
        print("pprice:", pprice[i])
        worksheet.write(i + 1, 1, str(pprice[i]))

    worksheet.write(0, 2, "商品狀態")
    for i in range(len(phave)):
        print("phave:", phave[i])
        worksheet.write(i + 1, 2, str(phave[i]))
# 如果需要查看 Data，可以使用以下代碼

# print("name:", pname, sep="")
# print("price:", pprice, sep="")
# print("have:", phave, sep="")

# 關閉瀏覽器
driver.close()
