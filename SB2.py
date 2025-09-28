from seleniumbase import SB
#chromedriver_path = "C:\\temp\\GoogleChromePortable64-132\\App\\Chrome-bin\\chrome.exe"
import random
import itertools
import datetime
import time


while 1 == 1:
   print("enter in a ZULU time 00:00 -> 23:59 (15:10) for 3:10pm")
   runtime = input()
   runtimearray = runtime.split(":")
   h = runtimearray[0]
   m = runtimearray[1]
   if ((h >= "00" and  h <= "23") and (m >= "00" and m <= "60")):
      break




#--------------------------------------------------------------------------------------------

with SB(test=True, uc=True) as sb:
    sb.open("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")
    #sb.type('[title="Search"]', "SeleniumBase GitHub page\n")
    #sb.click('[href*="github.com/seleniumbase/"]')
    #sb.save_screenshot_to_logs()  # ./latest_logs/
    print(sb.get_page_title())
    sb.click("#ctl00_ContentPlaceHolder1_btnAgree")
    #sb.wait_for_element("a[href='DispositionHome.aspx']")
    sb.wait_for_element_present("//a[contains(@href, 'Disposition')]", timeout=None)
    sb.click("//a[contains(@href, 'Disposition')]")
    print(sb.get_page_title())
    sb.click("//a[contains(@href, 'Acquire')]")
    print(sb.get_page_title())
    sb.click("//*[@id='ctl00_ContentPlaceHolder1_ddlDispositionType']/option[3]")
    print("dt")
    sb.click("//*[@id='ctl00_ContentPlaceHolder1_rblAcceptModifiedDisposition_0']")
    print("amd")
    while 1 == 1:
     timenow = datetime.datetime.now()
     showtime = timenow.strftime('%H:%M:%S')
     timetostart = timenow.strftime('%H:%M')
     print (showtime + "       " + timetostart + " -> " + runtime )
     if timetostart == runtime:
      sb.click("//*[@id='ctl00_lower_panel_btnContinue']")

      ## self.wait_for_element_present(selector, by="css selector", timeout=None)
      ## self.wait_for_element(selector, by="css selector", timeout=None)
      ## self.wait_for_element_visible(selector, by="css selector", timeout=None)
      #sb.wait_for_element_present(By.TITLE_TEXT,'Please confirm the disposition application has been filled out correctly before continuing.')
      
      ##sb.wait_for_element_present("//*[@title='Please confirm the disposition application has been filled out correctly before continuing.']")
      #sb.click("//*[@id='ctl00_lower_panel_btnContinue']")
      time.sleep(300)