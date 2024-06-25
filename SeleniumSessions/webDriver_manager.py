from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

browser_Name = input("Enter the browser name (Chrome/Firefox): ").strip()

if browser_Name == "Chrome":
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
elif browser_Name == "Firefox":
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
else:
    print('Please pass the correct browser name')
    raise Exception('Driver is not availabe :'+browser_Name)

driver.implicitly_wait(5)

driver.get("https://app.hubspot.com/login")
time.sleep(4)
driver.find_element(By.ID,'username').send_keys("Anandnayak812@gmail.com")
driver.find_element(By.ID,'password').send_keys("Anand@1111")
driver.find_element(By.ID,'loginBtn').click()
time.sleep(2)

print(driver.title)
def hello_World(value):
    print("Hello World from "+value)


driver.quit()


