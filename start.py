from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import random
import threading


def main():
    user_agent = random.choice(list(open('user-agents.txt')))
    user_agent = user_agent[0:-1]
    print(user_agent)

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
        firefox_profile=options, options=opt)
    # browser.get("https://2ip.ua")
    #browser.get("https://coub.com/view/2obtyt")
    #browser.get("http://rutracker.org")
    browser.get("https://www.youtube.com/watch?v=UIwhN3hHg7A")
    try:

        browser.find_element_by_css_selector("yt-formatted-string.size-small:nth-child(1)").click()

    except NoSuchElementException:
        print("Element Нет, спасибо not found")

    try:
         browser.find_element_by_xpath('/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form').click()
    except NoSuchElementException:
        print("Element Accept not found")
    # browser.find_element_by_class_name("ytp-play-button").click()

    # playElement = browser.find_element_by_class_name("play").click()
    time.sleep(2000)
    browser.close()
  


def start_app():
    for item in range(2):
        x = threading.Thread(target=main)
        x.start()
    time.sleep(60)


exit = False
counter = 0
while not exit:
    counter += 1
    if counter == 1:
        exit = True
    start_app()
