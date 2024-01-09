import json
import time
import os
import sys

from selenium  import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress','127.0.0.1:9222')

driver = webdriver.Chrome("c:\\Users\\cj\\.cache\\selenium\\chromedriver\\chromedriver.exe", options=options)

lang_map = {
    "日期": "date",
    "质量等级": "Quality grade",
    "轻度污染": "Mildly polluted",
    "中度污染": "Moderately polluted",
    '重度污染': 'Heavy pollution',
    "优": "Excellent",
    "良": "Good",
}

def get_month_data(city, month, path="."):
    print(f"get data {city} - {month}")
    driver.get(f'https://www.aqistudy.cn/historydata/daydata.php?city={city}&month={month}')
    time.sleep(2)
    tables = driver.find_elements(By.TAG_NAME, "table")
    data = []
    for table in tables:
        x = table.text.split()
        i = 9
        while i < len(x):
            k = range(9)
            item = dict()
            for j in k:
                name = x[j]
                if name in lang_map:
                    name = lang_map[name]
                value = x[i+j]
                if value in lang_map:
                    value = lang_map[value]
                item[name] = value
            data.append(item)
            print(data)
            i += 9
    if len(data) > 0:
        with open(f"{path}/{month}.json", "wt") as f:
            f.write(json.dumps(data))
    else:
        print(f"!!! no data for {city} @ {month} !!!")
    
def get_data(city):
    print(f"get data for {city}")
    path = f"../data/airquality/aqistudy/{city}"
    if not os.path.exists(path):
        os.makedirs(path)
    for year in range(2014, 2024):
        for month in range(12):
            ym = f"{year}{(month+1):02}"
            get_month_data(city, ym, path)

if __name__ == '__main__':
    if len(sys.argv)  < 2:
        print(f"usage: python get_aqistudy_data.py cityname")
    else:
        get_data(sys.argv[1])


