from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() 
prefs = {"download.default_directory" : "D:\Python Scripts\output"}
options.add_experimental_option("prefs",prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)

#Opening the website
driver.get('https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=')

#Unchecking preselected boxes
uncheck = ['//*[@id="ORIGIN_AIRPORT_ID"]', '//*[@id="ORIGIN_AIRPORT_SEQ_ID"]', '//*[@id="ORIGIN_CITY_MARKET_ID"]', '//*[@id="DEST_AIRPORT_ID"]', '//*[@id="DEST_AIRPORT_SEQ_ID"]', '//*[@id="DEST_CITY_MARKET_ID"]']
for checkbox in uncheck:
    driver.find_element(By.XPATH, checkbox).click() #untick the prexisting checkboxes
    
#Filtering
year = driver.find_element(By.XPATH, '//*[@id="cboYear"]') #Filtering Year 2021
dropdown1 = Select(year)
dropdown1.select_by_visible_text("2021") # select by visible text

geog = driver.find_element(By.XPATH, '//*[@id="cboGeography"]') #Filtering Geography California
dropdown2 = Select(geog)
dropdown2.select_by_visible_text("California") # select by visible text

#Checking Boxes
check = ['//*[@id="YEAR"]', '//*[@id="FL_DATE"]', '//*[@id="OP_CARRIER"]', '//*[@id="ORIGIN"]','//*[@id="DEP_DELAY"]','//*[@id="TAXI_OUT"]','//*[@id="ARR_DELAY_NEW"]','//*[@id="DISTANCE_GROUP"]','//*[@id="CARRIER_DELAY"]','//*[@id="WEATHER_DELAY"]','//*[@id="NAS_DELAY"]','//*[@id="SECURITY_DELAY"]', '//*[@id="LATE_AIRCRAFT_DELAY"]']
for checkbox in check:
    driver.find_element(By.XPATH, checkbox).click() 
    
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="btnDownload"]').click()
time.sleep(60)