#importing selenium web driver from selenium and chrome driver to use web scraping in chrome browser and By for targetting element ID

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#change this path to chrome driver location. chrome driver can be downloaded from https://sites.google.com/chromium.org/driver/
PATH = "C:\\Users\\M.SarfarazAlija1\\Downloads\\chromedriver_win32\\chromedriver.exe"

#using chrome as a browser and the web driver is located at PATH location
driver = webdriver.Chrome(PATH)

#calling google.com
driver.get('https://www.google.com/')

#multiple ways to find out element on web page, Id is being used here for accepting terms and conditions 
driver.find_element(By.ID, 'L2AGLb').click()

#getting searchbar for search query input
search = driver.find_element(By.TAG_NAME, "input")
search.send_keys('jafferyTech')
search.send_keys(Keys.RETURN)

#waiting for results to be shown in browser
try:
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rso"))
    )
    print(content)
    # searches = content.find_elements_by_class_name("Ww4FFb")
    # for article in searches:
    #     print(article.text)
except:
    driver.close()

#taking screenshot 
driver.save_screenshot('screen.png')

time.sleep(5)

driver.close()

