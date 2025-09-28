# import the required libraries
import undetected_chromedriver as uc
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
 
# define Chrome options
options = uc.ChromeOptions()

# set headless to False to run in non-headless mode
options.headless = False

cwd = os.getcwd()
print (cwd)
cwd = cwd.replace('\\', '/')
cwdchrome = cwd + "/chrome/GoogleChromePortable.exe"
print(cwdchrome)
# set up uc.Chrome(use_subprocess=True, options=options)
options.binary_location = cwdchrome
# Set the user data directory to save user info
cwdprofile = cwd + "/Data/profile"
print(cwdprofile)
options.add_argument("--user-data-dir=" + cwdprofile)
# Chrome driver
#driver = uc.Chrome(use_subprocess=True, options=options)
driver = uc.Chrome(version_main=132, use_subprocess=True, options=options)


 

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")



agree_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnAgree")
agree_button.click()

username_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtUsername")
username_field.click()
driver.execute_script("arguments[0].focus();", username_field)

action = ActionChains(driver) 
  
# perform the operation 
action.move_to_element(username_field).click().perform() 


#username_field.send_keys("_")
#username_field.send_keys("")
#password_field = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtPassword")
#login_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnLogin")
#driver.move_to_element(username_field).perform();
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
  if(len(runtimearray) == 3):
    break

while 2 == 2:
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




WebDriverWait(driver, 100).until(EC.element_to_be_clickable(("id","ctl00_lower_panel_btnContinue"))).click()

### here is the cloudflare

#try:
#WebDriverWait(driver, 100).until(EC.element_to_be_clickable(("id", "ctl00_lower_panel_btnContinue"))).click()
#except:
#  print("An exception occurred.")

#WebDriverWait(driver, 100).until(EC.presence_of_element_located(("xpath", '//button[text()="Confirm Application" and @class="btncontinue"]')))




