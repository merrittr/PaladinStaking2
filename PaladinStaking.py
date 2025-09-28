from seleniumbase import SB
#chromedriver_path = "C:\\temp\\GoogleChromePortable64-132\\App\\Chrome-bin\\chrome.exe"
import random
import itertools
import datetime
import time
import os
current_directory = os.getcwd()
chrome_binary_path = current_directory + "\\GoogleChromePortable64-138\\App\\Chrome-bin\\chrome.exe"

def clear_screen():
    # Check the operating system to determine the correct clear command
    if os.name == 'nt':  # 'nt' refers to Windows
        os.system('cls')
    else:  # 'posix' refers to Linux, macOS, and other Unix-like systems
        os.system('clear')
os.system('cls')
clear_screen()
print (os.name)
print ("cbp:" + chrome_binary_path)
#--------------------------------------------------------------------------------------------

#with SB(test=True, uc=True) as sb:
#with SB(test=True, uc=True, headed=True, browser="chrome") as sb:
with SB(test=True, uc=True, binary_location=chrome_binary_path) as sb:
    #sb.driver.binary_location = chrome_binary_path
    sb.open("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")
    print("1:" + sb.get_page_title())
    a = 1
    while 1 == 1:
     try:
      sb.wait_for_element_present('//*[@id="ctl00_ContentPlaceHolder1_btnAgree"]', timeout=None)
      break
     except Exception as e:
      print(f"An error occurred: {e}")
      print ("a" + a)
      a = a + 1 
       
     sb.click("#ctl00_ContentPlaceHolder1_btnAgree")
    #time.sleep(50)
    #sb.wait_for_element_present('//*[@id="ctl00_ContentPlaceHolder1_publicMapSearchSingle"]', timeout=None)
    #sb.wait_for_element_present("//a[contains(@alt, 'Disposition')]", timeout=None)
    x = 1
    while 1 == 1:
     try:
      elements = sb.find_elements("a")
      break
     except:
      print ("x:" + x)
      x = x + 1
       

    while 1 == 1:
     try:
      for element in elements:
       #print(element.text)
       if element.text == "Acquire a New Disposition":
        break
     except:
       break
       
    print("disposition")
  
    sb.click("//a[contains(@href, 'Disposition')]")
    print(sb.get_page_title())
    sb.click("//a[contains(@href, 'Acquire')]")
    print(sb.get_page_title())
    sb.click("//*[@id='ctl00_ContentPlaceHolder1_ddlDispositionType']/option[3]")
    print("dt")
    sb.click("//*[@id='ctl00_ContentPlaceHolder1_rblAcceptModifiedDisposition_0']")
    print("amd")


    while 1 == 1:
      print("enter in a ZULU time 00:00:00 -> 23:59:01 (15:10:01) for 3:10and 1 second pm")
      runtime = input()
      runtimearray = runtime.split(":")
      lenarray = len(runtimearray)
      if lenarray == 1:
       runtimearray.append("59")
       runtimearray.append("00")
       runtime = ":59:00"
      elif lenarray == 2:
        runtimearray.append("00")
        runtime = runtime + ":00"
      print(len(runtimearray))
     
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
      sb.click("//*[@id='imgValidate']")
      print("Image validated")
      item = sb.wait_for_element_present('//th[1][input[substring(@src, string-length(@src) - string-length("icon.png") + 1) = "icon.png"]]')
      print('text:', item.text)
      #time.sleep(3)
      #print("wait1 sec")
      #sb.wait_for_element_present("//*[@id='ctl00_lower_panel_btnContinue']", timeout=None)
      print("wait for continue button to be clickable ")
      #
      #sb.wait_for_element_clickable("//*[@id='ctl00_lower_panel_btnContinue']") 
      sb.click("//*[@id='ctl00_lower_panel_btnContinue']")
      print("continue button clicked")
      sb.wait_for_element_clickable("//*[@title='Confirm Application']", timeout=None)
      
      sb.click("//*[@title='Confirm Application']")
      sb.click("//button[text()='Yes' and @class='ui-button ui-corner-all ui-widget']")
      time.sleep(300)
