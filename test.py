from time import sleep
import undetected_chromedriver as uc
if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")
    sleep(50000)
    print(driver.title)