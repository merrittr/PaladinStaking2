# import the required libraries
import undetected_chromedriver as uc

 
# define Chrome options
options = uc.ChromeOptions()

# set headless to False to run in non-headless mode
options.headless = False

# set up the WebDriver for Chrome
driver = uc.Chrome(use_subprocess=True, options=options)

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


#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = uc.Chrome(use_subprocess=True, options=options)
driver.get("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")



agree_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnAgree")
agree_button.click()

#username_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtUsername")
#password_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtPassword")
#login_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnLogin")
#username_field.send_keys("merrittr")
#password_field.send_keys("Welcome2start!")
#login_button.click()

WebDriverWait(driver, 90).until(EC.presence_of_element_located(("id", "ctl00_ContentPlaceHolder1_btnViewPublicMap")))
###############################################################################################################################
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

WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("id","ctl00_ContentPlaceHolder1_btnContinue"))).click()

###############################################################################################################################


while 1 == 1:
   print("enter in a ZULU time 00:00 -> 23:59 (15:10) for 3:10pm")
   runtime = input()
   runtimearray = runtime.split(":")
   h = runtimearray[0]
   m = runtimearray[1]
   if ((h >= "00" and  h <= "23") and (m >= "00" and m <= "60")):
      break

while 1 == 1:
  timenow = datetime.datetime.now()
  showtime = timenow.strftime('%H:%M:%S')
  timetostart = timenow.strftime('%H:%M')
  print (showtime + "       " + timetostart + " -> " + runtime )
  if timetostart == runtime:
    break
WebDriverWait(driver, 100).until(EC.presence_of_element_located(("id","imgValidate"))).click()
time.sleep(1)
#continue_button = driver.find_element("id", "ctl00_lower_panel_btnContinue")
#continue_button.click()


#WebDriverWait(driver, 100).until(EC.presence_of_element_located(("id","ctl00_lower_panel_btnContinue"))).click()
WebDriverWait(driver, 100).until(EC.element_to_be_clickable(("id","ctl00_lower_panel_btnContinue"))).click()
## here is the cloudflare

#WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Confirm Application"]'))).click()
#time.sleep(5)


#WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, ".//button[contains(text(), 'Confirm')]"))).click()
#WebDriverWait(driver, 100).until(EC.presence_of_element_located(("id","ctl00_lower_panel_btnContinue"))).click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("id","ctl00_lower_panel_btnContinue"))).click()
#WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", '//button[text()="Confirm Application"]'))).click()

#WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, "ctl00_lower_panel_btnContinue"), "Confirm Application"))


#while 1 == 1:
# try:
##    ConfirmApplication = driver.find_element("xpath", '//button[text()="Confirm Application"]')
##    ConfirmApplication.click()
#  continue_button2 = driver.find_element("id", "ctl00_lower_panel_btnContinue")
#  continue_button2.click()
# except Exception as error:
#    print(error)






#driver.get("https://mars.isc.ca/MARSWeb/secure/disposition/DispositionHome.aspx")
#driver.get("https://mars.isc.ca/MARSWeb/secure/disposition/acquire/DispositionAcquire.aspx")

#c = 0
#while 1 == 1:
#  print (c)
#  c = c + 1
