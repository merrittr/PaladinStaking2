from seleniumbase import SB
import time
# You don't need itertools and random here at least as of now
chrome_binary_path = "C:\\temp\\GoogleChromePortable64-132\\App\\Chrome-bin\\chrome.exe"

with SB(test=True, uc=True, headed=True, browser="chrome") as sb:
    sb.driver.binary_location = chrome_binary_path
    sb.open("https://google.com/ncr")
    sb.type('[title="Search"]', "SeleniumBase GitHub page\n")
    sb.click('[href*="github.com/seleniumbase/"]')
    sb.save_screenshot_to_logs() # ./latest-logs/ 
    print(sb.get_page_title())
    time.sleep(300)