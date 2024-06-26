from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Specify the path to the Chrome WebDriver executable
chrome_driver_path = "C:\\Users\\E008148\\Downloads\\drivers\\chromedriver.exe"

# Configure Chrome options if needed
chrome_options = webdriver.ChromeOptions()
# Add options if needed, e.g., chrome_options.add_argument("--headless")

# Initialize Chrome WebDriver with service and options
driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path=chrome_driver_path), options=chrome_options)

# Open Google India website
driver.get("https://www.google.co.in/")
driver.find_element(By.NAME,'q').send_keys("Ronaldo")
time.sleep(3)
listofElements = driver.find_elements(By.XPATH,"//div[@class='aajZCb']//li//div/div[@class='lnnVSe']/div[starts-with(@class,'wM')]/span")

print(len(listofElements))
time.sleep(5)

for ele in listofElements:
    print(ele.text)
    if ele.text =='ronaldo net worth in rupees':
        ele.click()
        break

time.sleep(5)
# Perform further actions as needed
# print(driver.title)

