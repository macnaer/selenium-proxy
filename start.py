from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random


def main():
    user_agent = random.choice(list(open('user-agents.txt')))
    user_agent = user_agent[0:-1]
    print(user_agent)

    if "Macintosh;" in user_agent or "Windows" in user_agent:
        proxy = random.choice(list(open('proxy.txt')))
        proxy = proxy[0:-1]
        print(proxy)
        opt = Options()
        opt.headless = False
        options = webdriver.FirefoxProfile()

        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities["marrionette"] = True
        firefox_capabilities["proxy"] = {
            "proxyType": "MANUAL",
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy
        }

        options.set_preference("general.useragent.override", user_agent)

        browser = webdriver.Firefox(
            firefox_profile=options, options=opt, proxy=proxy)
        browser.get("https://2ip.ua")
        #browser.get("https://coub.com/view/2obtyt")
        # browser.get("https://rutracker.org")
        time.sleep(20)
        browser.close()
    # playElement = browser.find_element_by_class_name("play").click()


main()
