from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://app.hubspot.com/login")
driver.maximize_window()
wait = wd(driver,5)
user_Name = wait.until(ec.presence_of_element_located((By.ID,'username')))
user_Name.send_keys("AnandNayak@123")