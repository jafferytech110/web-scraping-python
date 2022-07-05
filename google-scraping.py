#importing selenium web driver from selenium and chrome driver to use web scraping in chrome browser and By for targetting element ID
# in this program i am using time implictly in order to keep program simple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#change this path to chrome driver location. chrome driver can be downloaded from https://sites.google.com/chromium.org/driver/
PATH = "C:\\Users\\fazi1\\Downloads\\chromedriver_win32\\chromedriver.exe"

# taking inputs
searchWord = input("Enter search Word :")
matriculationNumber = int(input('Enter your matriculation number last digit :'))

#using chrome as a browser and the web driver is located at PATH location
driver = webdriver.Chrome(PATH)

#calling google.com
driver.get('https://www.google.com/')

#multiple ways to find out element on web page, Id is being used here for accepting terms and conditions 
driver.find_element(By.ID, 'L2AGLb').click()

# checking search query number according to matriculation number last digit
searchNumber = 0

if(matriculationNumber != 9):
    searchNumber = matriculationNumber + 1

#getting searchbar for search query input
search = driver.find_element(By.TAG_NAME, "input")
search.send_keys(searchWord)
search.send_keys(Keys.RETURN)

time.sleep(3)

# saving results in results variable
results = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']/a")

if(len(results) < 1):
    print('Your search query has no result')
else:
    if(searchNumber > len(results)):
        results[0].click()
    else:
        results[searchNumber].click()

time.sleep(10)
#taking screenshot 
driver.save_screenshot('screen.png')

# extracting information of the page
title = driver.title
firstHeading = driver.find_element(By.TAG_NAME, 'h1')
secondHeading = driver.find_element(By.TAG_NAME, 'h2')

def printInformation(*args):
    for arg in args:
        if(type(arg) == str):
            print(arg)
        else:
            print(arg.text)

printInformation(title,firstHeading,secondHeading)

time.sleep(5)

driver.close()

