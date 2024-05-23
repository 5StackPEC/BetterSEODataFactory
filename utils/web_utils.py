from urllib.parse import urlparse
import json
from utils import web_utils

from selenium.webdriver.remote.webdriver import WebDriver


def get_site_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain_name = domain.split(".")[0]
    return domain_name


def take_screenshot(driver: WebDriver, url):
    driver.fullscreen_window()
    driver.save_screenshot(f"./dataset/images/{web_utils.get_site_name(url)}.png")


def load_js_script_to_driver(driver: WebDriver, js_script_path="./js/boundingBoxes.js"):
    with open(js_script_path, "r") as file:
        js_code = file.read()

    driver.execute_script(js_code)

    return driver
