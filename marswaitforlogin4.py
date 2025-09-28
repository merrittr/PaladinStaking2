#!C:\Users\RobMe\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from arcgis.gis import GIS
from arcgis.geometry import Point, Polyline, Polygon
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

import blinker as blink
import seleniumwire.undetected_chromedriver as uc

#import undetected_chromedriver as uc
driver = uc.Chrome(headless=True,use_subprocess=False)
#driver.get('https://nowsecure.nl')
#driver.save_screenshot('nowsecure.png')

#chrome_options = uc.ChromeOptions()
#chrome_options.add_argument('--blink-settings=imagesEnabled=false')


while 1 == 1:
   print("enter in a ZULU time 00:00 -> 23:59 (15:10) for 3:10pm")
   runtime = input()
   runtimearray = runtime.split(":")
   h = runtimearray[0]
   m = runtimearray[1]
   if ((h >= "00" and  h <= "23") and (m >= "00" and m <= "60")):
      break

user_agents = [
    # Add your list of user agents here
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
]

# select random user agent
user_agent = random.choice(user_agents)

# pass in selected user agent as an argument
options.add_argument(f'user-agent={user_agent}')

# Initialize the WebDriver
driver = uc.Chrome(options=options)


#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = webdriver.Chrome()
driver.get("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")





agree_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnAgree")
agree_button.click()




#username_field.send_keys(username)
#password_field.send_keys(password)
#login_button.click()

#ok_driver2 = WebDriverWait(driver, 10).until(driver.find_element("xpath", '//button[text()="Ok" and @class="ui-button ui-corner-all ui-widget"]'))

WebDriverWait(driver, 90).until(EC.presence_of_element_located(("id", "ctl00_ContentPlaceHolder1_btnViewPublicMap")))

#try:
#    ok_driver2 = driver.find_element("xpath", '//button[text()="Ok" and @class="ui-button ui-corner-all ui-widget"]')
#except:
#    while 1 == 1:
#        print("enter M.A.R.S. Password")
#        password = getpass()
#        username_field.send_keys(username)
#        password_field.send_keys(password)
#        login_button.click()
#        if (len(password.strip()) > 0):
#            break
    
#driver.get("https://mars.isc.ca/MARSWeb/secure/disposition/DispositionHome.aspx")
driver.get("https://mars.isc.ca/MARSWeb/secure/disposition/acquire/DispositionAcquire.aspx")



mySelect = Select(driver.find_element("id", "ctl00_ContentPlaceHolder1_ddlDispositionType"))
mySelect.select_by_index(2)



driver.find_element("id", "ctl00_ContentPlaceHolder1_rblAcceptModifiedDisposition_0").click()


#mySelect1 = Select(driver.find_element("id", "ctl00_ContentPlaceHolder1_lstAvailableClients"))
#mySelect1.select_by_index(0)
#driver.find_element("id", "ctl00_ContentPlaceHolder1_lstAvailableClients").click()
#driver.find_element("id", "ctl00_ContentPlaceHolder1_lstAvailableClients").click()


el = driver.find_element('id','ctl00_ContentPlaceHolder1_lstAvailableClients')
for option in el.find_elements(By.TAG_NAME,"option"): #el.find_elements_by_tag_name('option'):
    #if option.text == '2714 - Robert Wesley merritt (self)':
        option.click() # select() in earlier versions of webdriver
        break
    
    
assign_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnAssignClient")
assign_button.click()



pct_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_gvAssignedClients_ctl02_txtPercentage")
pct_field.send_keys(100)



submit_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnContinue")
submit_button.click()

map_field = driver.find_element("id", "divMap")
map_field.click()

print (str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute))

#while 1 == 1:
#  timetostart = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)#
  #print (timetostart)
#  if timetostart == "14:9":
#    break





while 1 == 1:
  timenow = datetime.datetime.now()
  timetostart = timenow.strftime('%H:%M')
  print (timetostart)
  if timetostart == runtime:
    break



continue_button = driver.find_element("id", "ctl00_lower_panel_btnContinue")
continue_button.click()


time.sleep(5)
#WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Widget containing a Cloudflare security challenge']")))
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='cb-lb']"))).click()


WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='Widget containing a Cloudflare security challenge']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.cb-lb"))).click()

continue_button2 = driver.find_element("id", "ctl00_lower_panel_btnContinue")
continue_button2.click()




element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')))


element1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')))


yes_driver3 = driver.find_element("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')
yes_driver3.click()
