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
driver.get("https://www.londonfreelance.org/courses/frames/index.html")
time.sleep(5)
driver.switch_to.frame(2)
title = driver.find_element(By.XPATH,"//h2[text()='Title bar ']")
print(title.text)
time.sleep(4)