from seleniumbase import Driver
seleniumbase get chromedriver


# initialize driver with UC Mode enabled

#https://www.zenrows.com/blog/undetected-chromedriver-alternatives#seleniumbase-uc

from seleniumbase.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:/temp/GoogleChromePortable64-132/GoogleChromePortable.exe"
# you may need some other options
#options.add_argument('--no-sandbox')
#options.add_argument('--no-default-browser-check')
#options.add_argument('--no-first-run')
#options.add_argument('--disable-gpu')
#options.add_argument('--disable-extensions')
#options.add_argument('--disable-default-apps')




#driver = Driver(uc=True)
#driver = Driver(uc=True, options=options, "C:/temp/GoogleChromePortable64-132/GoogleChromePortable.exe")
driver = Driver(uc=True, options=options)

# target URL
url = "https://gitlab.com/users/sign_in"

# open URL using UC Mode's reconnect feature
# 4 seconds reconnection time to avoid detection
driver.uc_open_with_reconnect(url, 4)

# capture screenshot
driver.save_screenshot("gitlab_screenshot.png")

# close the browser and end the session
driver.quit()