from urllib.parse import urlparse
import json
from utils import web_utils

from selenium.webdriver.remote.webdriver import WebDriver


def get_site_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain_name = domain.split(".")[0]
    return domain_name


def write_json_annotation(annotation):
    with open("./dataset/annotations/annotations.json", "w") as json_file:
        json.dump(annotation, json_file)


def take_screenshot(driver: WebDriver, url):
    driver.fullscreen_window()
    driver.save_screenshot(f"./dataset/images/{web_utils.get_site_name(url)}.png")
