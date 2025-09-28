from seleniumbase import SB
#chromedriver_path = "C:\\temp\\GoogleChromePortable64-132\\App\\Chrome-bin\\chrome.exe"
import random
import itertools
import datetime
import time
import os

def clear_screen():
    # Check the operating system to determine the correct clear command
    if os.name == 'nt':  # 'nt' refers to Windows
        os.system('cls')
    else:  # 'posix' refers to Linux, macOS, and other Unix-like systems
        os.system('clear')
os.system('cls')
print (os.name)
clear_screen()

#--------------------------------------------------------------------------------------------

with SB(test=True, uc=True) as sb:
    sb.open("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")
    print(sb.get_page_title())
    sb.click("#ctl00_ContentPlaceHolder1_btnAgree")
    time.sleep(10)
    #sb.wait_for_element_present('//*[@id="ctl00_ContentPlaceHolder1_publicMapSearchSingle"]', timeout=None)
    sb.wait_for_element_present("//a[contains(@alt, 'Disposition')]", timeout=None)
    elements = sb.find_elements("a")
    for element in elements:
     print(element.text)



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
      sb.click("//*[@id='ctl00_lower_panel_btnContinue']")
      sb.wait_for_element_present("//*[@title='Confirm Application']", timeout=None)
      sb.click("//*[@title='Confirm Application']")
      time.sleep(300)