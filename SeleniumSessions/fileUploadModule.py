from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
time.sleep(5)
driver.find_element(By.NAME,'upfile').send_keys("C:/Users/E008148/Downloads/Hospital Bill.pdf")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(3)