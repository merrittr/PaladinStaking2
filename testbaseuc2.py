from seleniumbase import Driver as sbDriver


    
    # Get folder path of the Documents
    chromedriver_path = "C:/temp/GoogleChromePortable64-132/GoogleChromePortable.exe"
    driver = sbDriver(
                          headless=headless,
                          agent=user_agent,
                          binary_location=chromedriver_path
                          )



    url = "https://www.differencebetween.com/difference-between-atomic-mass-and-vs-molecular-weight/"                      
    driver.get(url)
    driver.maximize_window()