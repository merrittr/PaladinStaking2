from seleniumbase import SB
#chromedriver_path = "C:\\temp\\GoogleChromePortable64-132\\App\\Chrome-bin\\chrome.exe"
import random
import itertools
import time
import tkinter as tk
from tkinter import ttk


#--------------------------------------------------------------------------------------------
def get_selected_time():
    hour = hour_spinbox.get()
    minute = minute_spinbox.get()
    print(f"Selected Time: {hour}:{minute}")
    return str(hour), str(minute)  # Returns a tuple implicitly

# Create the main window
root = tk.Tk()
root.title("Time Selector")

# Create Spinbox for hours
hour_label = ttk.Label(root, text="Hour:")
hour_label.grid(row=0, column=0, padx=5, pady=5)
hour_spinbox = ttk.Spinbox(root, from_=0, to_=23, wrap=True, width=3)
hour_spinbox.set("00") # Set initial value
hour_spinbox.grid(row=0, column=1, padx=5, pady=5)

# Create Spinbox for minutes
minute_label = ttk.Label(root, text="Minute:")
minute_label.grid(row=0, column=2, padx=5, pady=5)
minute_spinbox = ttk.Spinbox(root, from_=0, to_=59, wrap=True, width=3)
minute_spinbox.set("00") # Set initial value
minute_spinbox.grid(row=0, column=3, padx=5, pady=5)

# Create a button to get the selected time
select_button = ttk.Button(root, text="Select Time", command=get_selected_time)
select_button.grid(row=1, column=0, columnspan=4, pady=10)

# Run the Tkinter event loop
hour = "99"
minute = "99"
if (not(hour >= "00" and  hour <= "23") and not(minute >= "00" and minute <= "60")):
      hour, minute = root.mainloop()
      print(f"1 Selected Time: {hour}:{minute}")
      print(not(hour >= "00" and  hour <= "23"))
      print(not(minute >= "00" and minute <= "60"))
print(f"2 Selected Time: {hour}:{minute}")
#--------------------------------------------------------------------------------------------

with SB(test=True, uc=True) as sb:
    sb.open("https://mars.isc.ca/MARSWeb/TermsOfService.aspx?ReturnURL=%7e%2fLogin.aspx&Exp=638468865082721610&Digest=ppuiBjVYPKmNcpnBNoAnCg")
    #sb.type('[title="Search"]', "SeleniumBase GitHub page\n")
    #sb.click('[href*="github.com/seleniumbase/"]')
    #sb.save_screenshot_to_logs()  # ./latest_logs/
    print(sb.get_page_title())
    sb.click("#ctl00_ContentPlaceHolder1_btnAgree")
    time.sleep(60)
    #sb.wait_for_element("a[href='DispositionHome.aspx']")
    sb.wait_for_element("//a[contains(@href, 'Disposition')]")
    sb.click("//a[contains(@href, 'Disposition')]")
    print(sb.get_page_title())
    sb.click("//a[contains(@href, 'Acquire')]")
    print(sb.get_page_title())
    sb.click("//*[@id='ctl00_ContentPlaceHolder1_ddlDispositionType']/option[3]")
    print("dt")
    sb.click("//*[@id='ctl00_ContentPlaceHolder1_rblAcceptModifiedDisposition_0']")
    print("amd")
    
    time.sleep(300)