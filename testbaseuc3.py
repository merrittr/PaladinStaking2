from seleniumbase import SB
chromedriver_path = "C:\\temp\\GoogleChromePortable64-132\\App\\Chrome-bin\\chrome.exe"
import random
import itertools

def user_agent_rotator(user_agent_list):
    # shuffle the User Agent list
    random.shuffle(user_agent_list)
    # rotate the shuffle to ensure all User Agents are used
    return itertools.cycle(user_agent_list)


# define Chrome options
#options = SB.ChromeOptions()

# create a User Agent list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    # ... add more User Agents
]

# initialize a generator for the User Agent rotator
user_agent_cycle = user_agent_rotator(user_agents)

with SB(test=True, uc=True) as sb:
    sb.open("https://google.com/ncr")
    sb.type('[title="Search"]', "SeleniumBase GitHub page\n")
    sb.click('[href*="github.com/seleniumbase/"]')
    sb.save_screenshot_to_logs()  # ./latest_logs/
    print(sb.get_page_title())