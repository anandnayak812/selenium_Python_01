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
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(3)
alertType = driver.switch_to.alert
print(alertType.text)
alertType.accept()
time.sleep(3)

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(3)
print(alertType.text)
alertType.send_keys("Anand Nayak")
alertType.accept()
time.sleep(3)

