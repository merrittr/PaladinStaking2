#!C:\Users\RobMe\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from arcgis.gis import GIS
from arcgis.geometry import Point, Polyline, Polygon
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

#import blinker as blink
#import seleniumwire.undetected_chromedriver as uc

import undetected_chromedriver as uc
driver = uc.Chrome(headless=True,use_subprocess=False)
#driver.get('https://nowsecure.nl')
#driver.save_screenshot('nowsecure.png')