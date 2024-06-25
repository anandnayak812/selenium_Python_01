from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()

def select_Options(element,value):
    if not value[0]=='all':
        time.sleep(2)
        for a in element:
            print(a.text)
            for c in range(len(value)):
                if a.text == value [c]:
                    a.click()
                    time.sleep(2)
                    break
    else:
        try:
            for ele in element:
                ele.click()
        except Exception as e:
            print(e)


driver.find_element(By.XPATH,"//input[@id='justAnInputBox']").click()
time.sleep(3)
getList = driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
value_List = ['choice 5','choice 6','choice 6 1']
# select_Options(getList,['all'])
select_Options(getList,value_List)