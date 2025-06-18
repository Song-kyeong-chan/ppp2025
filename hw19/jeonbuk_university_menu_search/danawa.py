import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

class DanawaSearch:
    def __init__(self):
        options = ChromeOptions()
        options.add_argument("headless")
        self.driver = Chrome(options=options)

    def get_data(self, address_list):
        temp_list = []
        for l in address_list:
            self.driver.get(l)
            time.sleep(2)
            response = self.driver.page_source
            soup = BeautifulSoup(response, "html.parser")

            try:
                product_name = soup.find("div", {"class": "top_summary"}).find("h3", {"class": "prod_tit"}).text.strip()
                table = soup.find("tbody", {"class": "high_list"})
                low_price_module = table.find("tr", {"class": "cash_lowest"})
                is_cash = "현금"
                if low_price_module is None:
                    low_price_module = table.find("tr", {"class": "lowest"})
                    is_cash = ""
                product_price = low_price_module.find("em", {"class": "prc_t"}).text.strip()
                ship_price = low_price_module.find("span", {"class": "stxt"}).text.strip()
                link = low_price_module.find("a").get("href")
                self.driver.find_element(By.CLASS_NAME, "smr_graph").screenshot("test1.png")

                temp_dict = {
                    "product_name": product_name,
                    "product_price": product_price,
                    "ship_price": ship_price,
                    "is_cash": is_cash,
                    "link": link,
                }
                temp_list.append(temp_dict)
            except Exception as e:
                print(f"❌ 오류 발생: {l} -> {e}")
        return temp_list

    def __del__(self):
        self.driver.quit()

product_links = [
    "https://prod.danawa.com/info/?pcode=15736046",
    "https://prod.danawa.com/info/?pcode=17473238"
]

ds = DanawaSearch()
result = ds.get_data(product_links)
df = pd.DataFrame(result)
df.to_csv("danawa_price_data.csv", index=False, encoding="utf-8-sig")
print("✅ danawa_price_data.csv 저장 완료")
