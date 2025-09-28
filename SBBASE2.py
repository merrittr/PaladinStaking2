from seleniumbase import SB
import time
chrome_binary = "C:\\temp\\GoogleChromePortable64-132\\App\\Chrome-bin\\chrome.exe"

with SB(test=True, uc=True, binary_location=chrome_binary) as sb:
    sb.open("https://google.com/ncr")
    sb.type('[title="Search"]', "SeleniumBase GitHub page\n")
    sb.click('[href*="github.com/seleniumbase/"]')
    sb.save_screenshot_to_logs()  # ./latest_logs/
    print(sb.get_page_title())

    time.sleep(300)