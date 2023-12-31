# Wrote by: 蔡岳哲
# From: 高雄師範大學 軟體系三年級
# 學號(id): 411077010
# 開發時間: 2023年11月~2024年1月
# 爬蟲工具: 可抓取資料名稱、筆數、價格、存貨量...等
# 預設瀏覽器: chrome
# 測試時使用chrome版本: 120.0.6099.109
# 使用的爬蟲工具: webdriver(chromedriver.exe)
# webdriver相對路徑: .\\final project\\chromedriver.exe
# 測試用網址: https://ecshweb.pchome.com.tw/search/v3.3/?q=corsair&scope=all
# %20為pchome預設的空格輸入
# 測試時網速: 60Mbps

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import xlsxwriter

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--enable-chrome-browser-cloud-management")
chrome_options.add_argument(
    "webdriver.chrome.driver=.\\final project\\chromedriver.exe"
)
driver = webdriver.Chrome(options=chrome_options)

# 輸入的網址
driver.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=corsair&scope=all")


# 等待一段時間，讓網頁充分加載
sleep(1.5)
driver.maximize_window()
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
sleep(1)

# 用soup套件渲染html資料
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# 先抓取網頁上顯示的全部資料筆數
product_num_elements = soup.find_all("div", class_="msg_box")
for num in product_num_elements:
    value_elements = num.find_all("span", class_="value")

    for value_element in value_elements:
        totalNum = value_element.text.strip()
        # 全部資料筆數(測試用輸出):
        print("網站上的資料筆數", totalNum)

# 滾動頁面在pchome設定中至多顯示20筆資料
# 由於在測試中約1.2秒可以完整顯示出20筆資料，因此設定1.2秒作為間隔
# 用上面所得totalNum，除以每次滾動可抓取20筆資料再加上1，作為迴圈的次數，便大約可抓取全部資料
# 若有遺漏，多為網速太慢所致，但可忽略，因為最後的資料與使用者所需大多不相符
# 若要完整呈現，可將58行的sleep數字改大
for i in range(int(totalNum) // 20 + 2):
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    sleep(1.2)

# 再次用soup套件渲染html資料
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
    if product_name_tag:
        for product_name in product_name_tag:
            # Use .text.strip() to get the stripped text
            name = product_name.text.strip()

            # 將數據添加到 Datalist
            pname.append(name)
            # 測試用輸出:
            # print(name)
    else:
        pname.append("未找到該名稱產品")

    # 提取價格
    price = block.find_all("span", class_="price")
    for price_uni in price:
        # Use .text.strip() to get the stripped text
        price_unique = price_uni.text.strip()

        # 將數據添加到 Datalist
        pprice.append(price_unique)
        # 測試用輸出:
        # print(price_unique)

    # 是否有貨
    button_tag = block.find_all("button", class_="unblock")
    for button in button_tag:
        # Use .text.strip() to get the stripped text
        button_uni = button.text.strip()
        # 將數據添加到 Datalist
        phave.append(button_uni)
        # 測試用輸出:
        # print(button_uni)


# 將 DataFrame 寫入 Excel 文件
with xlsxwriter.Workbook(".\\final project\\product_data.xlsx") as workbook:
    worksheet = workbook.add_worksheet()

    # 產品名稱
    worksheet.write(0, 0, "產品名稱")
    for i in range(len(pname)):
        # 測試用輸出:
        # print("pname:", pname[i])
        worksheet.write(i + 1, 0, str(pname[i]))

    # 價格
    worksheet.write(0, 1, "價格")
    for i in range(len(pprice)):
        # 測試用輸出:
        # print("pprice:", pprice[i])
        worksheet.write(i + 1, 1, str(pprice[i]))

    # 商品狀態
    worksheet.write(0, 2, "商品狀態")
    for i in range(len(phave)):
        # 測試用輸出:
        # print("phave:", phave[i])
        worksheet.write(i + 1, 2, str(phave[i]))

    # 資料筆數
    worksheet.write(0, 3, "資料筆數:")
    total = len(pname)
    worksheet.write(1, 3, total)

    # 商品平均價格
    worksheet.write(0, 4, "商品平均價格:")
    total_price = 0
    for i in range(len(pprice)):
        total_price += int(pprice[i][1:])
    total_price /= len(pprice)
    worksheet.write(1, 4, round(total_price, 2))

    # 有現貨數
    worksheet.write(0, 5, "有現貨數(可加入購物車):")
    total_product = 1
    for i in range(len(phave)):
        if phave[i] == "加入購物車":
            total_product += 1
    worksheet.write(1, 5, total_product)

    # 有現貨趴數(百分比)
    worksheet.write(0, 6, "有現貨數(可加入購物車)百分比:")
    total_product_percentage = round(total_product * 100 / total, 2)
    worksheet.write(1, 6, total_product_percentage)

    # 可訂購數
    worksheet.write(0, 7, "可訂購數(立即訂購):")
    total_order = 1
    for i in range(len(phave)):
        if phave[i] == "立即訂購":
            total_order += 1
    worksheet.write(1, 7, total_order)

    # 可訂購趴數(百分比)
    worksheet.write(0, 8, "可訂購數百分比:")
    total_order_percentage = round(total_order * 100 / total, 2)
    worksheet.write(1, 8, total_order_percentage)

    # 缺貨數
    worksheet.write(0, 9, "缺貨數(售完，補貨中！):")
    total_soldout = 1
    for i in range(len(phave)):
        if phave[i] == "售完，補貨中！":
            total_soldout += 1
    worksheet.write(1, 9, total_soldout)

    # 缺貨趴數(百分比)
    worksheet.write(0, 10, "缺貨數百分比:")
    total_soldout_percentage = round(total_soldout * 100 / total, 2)
    worksheet.write(1, 10, total_soldout_percentage)

# 如果需要查看 Data，可以使用以下代碼(測試用輸出):

# print("name:", pname, sep="")
# print("price:", pprice, sep="")
# print("have:", phave, sep="")

# 資料筆數
print("抓取的資料筆數", len(pname))

# 關閉瀏覽器
driver.close()
