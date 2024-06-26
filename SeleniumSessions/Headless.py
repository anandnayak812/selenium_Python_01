from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoAlertPresentException
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Ensure headless mode is enabled
options.add_argument("--incognito")
options.add_argument("--disable-gpu")  # Disable GPU acceleration (useful in headless mode)
options.add_argument("--no-sandbox")  # Bypass OS security model (useful for certain environments)
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/")
print(driver.title)