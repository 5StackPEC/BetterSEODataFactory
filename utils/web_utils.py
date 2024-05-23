from urllib.parse import urlparse
import json
from utils import web_utils
import tldextract

# types
from selenium.webdriver.remote.webdriver import WebDriver


def get_site_name_old(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain_name = domain.split(".")[0]
    return domain_name


def get_site_name(url):
    return tldextract.extract(url).domain


def take_screenshot_of_window(driver: WebDriver, url):
    # The url is only needed for the file name, it does not actually uses it!
    driver.fullscreen_window()
    driver.save_screenshot(f"./dataset/images/{web_utils.get_site_name(url)}.png")
    driver.maximize_window()
