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


while 1 == 1:
   print("enter M.A.R.S. Username")
   username = input()
   if (len(username.strip()) > 0):
      break

while 1 == 1:
   print("enter M.A.R.S. Password")
   password = getpass()
   if (len(password.strip()) > 0):
      break


while 1 == 1:
   print("enter in a ZULU time 00:00 -> 23:59 (15:10) for 3:10pm")
   runtime = input()
   runtimearray = runtime.split(":")
   h = runtimearray[0]
   m = runtimearray[1]
   if ((h >= "00" and  h <= "23") and (m >= "00" and m <= "60")):
      break





driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")





agree_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnAgree")
agree_button.click()

username_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtUsername")
password_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtPassword")
login_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnLogin")
username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()


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
continue_button2 = driver.find_element("id", "ctl00_lower_panel_btnContinue")
continue_button2.click()

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')))
#element.click()
#yes_driver2 = driver.find_element("xpath", '//button[contains(text(), "Yes")]')
#yes_driver2.click()

element1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')))
yes_driver3 = driver.find_element("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')
yes_driver3.click()
