from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://library.usask.ca/#gsc.tab=0")

wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "primoQueryTemp").send_keys("elon musk")
#driver.find_element(By.CSS_SELECTOR, "button[title='Search']").click()

#links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "h3 > a")))
#for link in links:
#    print(link.text)


    # Keep the browser open for observation
time.sleep(566)

# Close the driver
driver.quit()