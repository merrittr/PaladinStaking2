# import the required libraries
import undetected_chromedriver as uc

 
# define Chrome options
options = uc.ChromeOptions()

#https://www.zenrows.com/blog/undetected-chromedriver-user-agent#rotate-user-agent
#https://www.zenrows.com/blog/undetected-chromedriver-cloudflare#alternative

# set headless to False to run in non-headless mode
options.headless = False

# set up uc.Chrome(use_subprocess=True, options=options)

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
from selenium.webdriver.common.action_chains import ActionChains 

options.binary_location = "C:/temp/GoogleChromePortable64-132/GoogleChromePortable.exe"
# Set the user data directory to save user info
options.add_argument("--user-data-dir=C:/temp/GoogleChromePortable64-132/Data/profile")
# Chrome driver
#driver = uc.Chrome(use_subprocess=True, options=options)
driver = uc.Chrome(version_main=131, use_subprocess=True, options=options)


driver.get("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")



agree_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnAgree")
agree_button.click()

username_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtUsername")
username_field.click()
driver.execute_script("arguments[0].focus();", username_field)

action = ActionChains(driver) 
  
# perform the operation 
action.move_to_element(username_field).click().perform() 



WebDriverWait(driver, 90).until(EC.presence_of_element_located(("id", "ctl00_ContentPlaceHolder1_btnViewPublicMap")))
###############################################################################################################################
driver.get("https://mars.isc.ca/MARSWeb/secure/disposition/acquire/DispositionAcquire.aspx")
mySelect = Select(driver.find_element("id", "ctl00_ContentPlaceHolder1_ddlDispositionType"))
mySelect.select_by_index(2)



driver.find_element("id", "ctl00_ContentPlaceHolder1_rblAcceptModifiedDisposition_0").click()


select = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lstAvailableClients"))

num_options = len(select.options)
print(num_options)


selectnum = "0"
if num_options > 1:
  for x in range(num_options):
    print ("Enter the number " + str(x) + " FOR:" +select.options[x].text)
  while 1 == 1:
    selectnum = input()
    if (int(selectnum) >= 0 and  int(selectnum) <= num_options - 1):
      break
    else:
      for x in range(num_options):
        print ("Try again Enter the number " + str(x) + " FOR:" +select.options[x].text)

el = driver.find_element('id','ctl00_ContentPlaceHolder1_lstAvailableClients')
for option in el.find_elements(By.TAG_NAME,"option"): #el.find_elements_by_tag_name('option'):
    if option.text == select.options[int(selectnum)].text: #'2714 - Robert Wesley merritt (self)':
        option.click() # select() in earlier versions of webdriver
        break

    
    
assign_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnAssignClient")
assign_button.click()



pct_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_gvAssignedClients_ctl02_txtPercentage")
pct_field.send_keys(100)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("id","ctl00_ContentPlaceHolder1_btnContinue"))).click()

###############################################################################################################################


while 1 == 1:
   print("enter in a ZULU time 00:00:00 -> 23:59:01 (15:10:01) for 3:10and 1 second pm")
   runtime = input()
   runtimearray = runtime.split(":")
   h = runtimearray[0]
   m = runtimearray[1]
   s = runtimearray[2]
   if ((h >= "00" and  h <= "23") and (m >= "00" and m <= "60") and (s >= "00" and s <= "60")):
      break

while 1 == 1:
  timenow = datetime.datetime.now()
  showtime = timenow.strftime('%H:%M:%S')
  timetostart = timenow.strftime('%H:%M:%S')
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
time.sleep(1)
WebDriverWait(driver, 100).until(EC.element_to_be_clickable(("id", "ctl00_lower_panel_btnContinue"))).click()
#continue_button = driver.find_element("id", "ctl00_lower_panel_btnContinue")
#continue_button.click()
#continue_button2 = driver.find_element("id", "ctl00_lower_panel_btnContinue")
#continue_button2.click()

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')))
#element.click()
#yes_driver2 = driver.find_element("xpath", '//button[contains(text(), "Yes")]')
#yes_driver2.click()

element1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')))
yes_driver3 = driver.find_element("xpath", '//button[text()="Yes" and @class="ui-button ui-corner-all ui-widget"]')
yes_driver3.click()




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
