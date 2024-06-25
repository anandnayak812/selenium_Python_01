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
driver.get("https://demo.automationtesting.in/Static.html")
time.sleep(5)

source = driver.find_element(By.ID,"angular")
destination = driver.find_element(By.ID,'droparea')
actions = ActionChains(driver)
actions.scroll_to_element(source).perform()
time.sleep(5)
# actions.drag_and_drop(source,destination).perform()
actions.click_and_hold(source).move_to_element(destination).release().perform()
time.sleep(5)