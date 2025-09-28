# Import the required libraries
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
import time

# Define Chrome options
options = uc.ChromeOptions()

# Set headless to False to run in non-headless mode
options.headless = False
# Set the binary location of the browser

#131
#"C:\\temp\\GoogleChromePortable64-131\\GoogleChromePortable.exe"
#"C:\\temp\\GoogleChromePortable64-131\\App\\Chrome-bin\\chrome.exe"
#114
#"C:\\temp\\GoogleChromePortable64-114\\GoogleChromePortable.exe"
#"C:\\temp\\GoogleChromePortable64-114\\App\\Chrome-bin\\chrome.exe"


options.binary_location = "C:\\temp\\GoogleChromePortable64-114\\GoogleChromePortable.exe"
# Set the user data directory to save user info
options.add_argument("--user-data-dir=C:\\temp\\GoogleChromePortable64-114\\Data\\profile")
# Chrome driver
driver = uc.Chrome(version_main=131,use_subprocess=True, options=options)

# Go to the desired URL
driver.get("https://library.usask.ca/#gsc.tab=0")

# Wait until the input field is visible
wait = WebDriverWait(driver, 10)
q_field = wait.until(EC.presence_of_element_located((By.ID, "primoQueryTemp")))

# Use JavaScript to focus the element
driver.execute_script("arguments[0].focus();", q_field)

# Initiate typing into the field
q_field.send_keys("_")

# Click the field to trigger any other events
q_field.click()

# Keep the browser open for observation
time.sleep(60)

# Close the driver
driver.quit()