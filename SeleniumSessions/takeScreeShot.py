from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/")
# time.sleep(5)
# driver.get_screenshot_as_file("amazon_File.png")
# To get the Full Page as Screen Shot
A = lambda S: driver.execute_script("return document.body.parentNode.scroll"+S)
driver.set_window_size(A('Width'),A('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('amazon_full.png')
time.sleep(2)