# Get Data
Some data is published in single file, such as [WDI_CSV.zip](https://databank.worldbank.org/data/download/WDI_CSV.zip), [air-pollution.csv](https://ourworldindata.org/explorers/air-pollution), [IHME-GBD_2019_DATA-51e8c8b5-1.zip](https://vizhub.healthdata.org/gbd-results/result/51e8c8b53699bd42c1652111ab38a07f) etc., which could be downloaded directly through a few clicks.

However, some data, such air quality report, are release daily, monthly, and scattered in lots of different pages, which is difficult to download manually and have to resort to tools and scripts.
## Get Data with selenium and scripts.
[selenium](https://www.selenium.dev/) is a project for a range of tools and libraries that enable and support the automation of web browsers. Here a summary of steps for retrieving data with selenium.
### install required tools:
```
pip install selenium
```

### start chrome in debug mode:
* windows
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir=C:\\Users\\cj
```
* linux
```
/opt/google/chrome/chrome --remote-debugging-port=9222 --user-data-dir=/mnt/c/User/sj &
```

### run script to control chome to open page
1. import required libraries
```python
import json
import time
import os
import sys

from selenium  import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
```
2. start the session
```python
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
```

3. control the browser
```python
url="https://ourworldindata.org/explorers/air-pollution"
driver.get(url)
time.sleep(5)

action_buttons = driver.find_elements(By.CLASS_NAME, "ActionButtons")
buttons = action_buttons[0].find_elements(By.TAG_NAME, "button")
driver.execute_script("arguments[0].scrollIntoView();", buttons[0])
time.sleep(1)

buttons[0].click()
time.sleep(3)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
time.sleep(3)

buttons = driver.find_elements(By.CLASS_NAME, "grouped-menu-item")
time.sleep(1)
buttons[2].click()
time.sleep(5)

driver.get('chrome://downloads')
```
### lesson learned
1. chromedriver's version must be matched with chrome's version
2. in case chrome does not action during script running, it could try to close all chrome instances before start debug mode chome, also could check if the port is occupied by other application.

# Data Process
## WDIData.csv
WDIData.csv in WDI_CSV contains lots of data and a wide date range (1960 ~ 2022), to filter out the data for our project and date range within 1990 through 2022, a script is written for filtering out interested data.

## air-pollution.csv
similary, [air-pollution.csv](https://ourworldindata.org/explorers/air-pollution) contains data with wide date range (1750-2022). also a couple of contries name are different with those in WDIData.csv, a script is written for filtering out interested data, also use the save country name as in WDIData.csv.

## IHME-GBD_2019_DATA-51e8c8b5-1.zip
[IHME-GBD_2019_DATA](https://vizhub.healthdata.org/gbd-results/result/51e8c8b53699bd42c1652111ab38a07f) contains death rate caused by Respiratory infections and tuberculosis and Respiratory infections and tuberculosis

Here a list of countries which name are different for those in WDIData.csv.
```python
country_alias = {
    "egypt":"egypt, arab rep.",
    "europe":"european union",
    "faeroe islands":"faroe islands",
    "gambia":"gambia, the",
    "french guiana":"guinea",
    "high-income countries":"high income",
    "hong kong":"hong kong sar, china",
    "iran":"iran, islamic rep.",
    "north korea":"korea, dem. people's rep.",
    "south korea":"korea, rep.",
    "laos":"lao pdr",
    "low-income countries":"low income",
    "micronesia (country)":"micronesia, fed. sts.",
    "russia":"russian federation",
    "slovakia":"slovak republic",
    "saint kitts and nevis":"st. kitts and nevis",
    "saint lucia":"st. lucia",
    "syria":"syrian arab republic",
    "timor":"timor-leste",
    "turkey":"turkiye",
    "upper-middle-income countries":"upper middle income",
    "venezuela":"venezuela, rb",
    "vietnam":"viet nam",
    "united states virgin islands":"virgin islands (u.s.)",
    "yemen":"yemen, rep.",
}
```
#




