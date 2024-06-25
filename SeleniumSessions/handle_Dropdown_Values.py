from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
# import webDriver_manager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
time.sleep(4)
country_List = driver.find_element(By.XPATH, '//p/select')

getValue = Select(country_List)
# getValue.select_by_visible_text("India")
getAllCountry = getValue.options
for i in getAllCountry:
    print(i.text)
    if i.text=="Australia":
        time.sleep(2)
        i.click()
        break


def select_Method(element, country):
    select = Select(element)
    select.select_by_visible_text(country)


select_Method(country_List, "India")


# import  webDriver_manager.hello_World("Anand")
