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
driver.get("https://www.spicejet.com/")
time.sleep(5)
# driver.switch_to.alert.accept()
action_element = ActionChains(driver)
addOn = driver.find_element(By.XPATH,"//div[text()='Add-ons']")
action_element.move_to_element(addOn).perform()
time.sleep(2)

driver.find_element(By.XPATH, "//a[@data-testid='test-id-SpiceMax']/div/div[text()='SpiceMax']").click()

time.sleep(5)
