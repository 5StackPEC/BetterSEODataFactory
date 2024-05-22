from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import json
from tqdm import tqdm
from utils import visual_utils

# types
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


def initialized_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    return driver


def initialized_js_script(driver: WebDriver, js_script_path = "./js/boundingBoxes.js"):
    with open("./js/boundingBoxes.js", "r") as file:
        js_code = file.read()

    driver.execute_script(js_code)

    return driver


def generate_annotation_from_url(driver: WebDriver, url):
    driver.get(url)
    initialized_js_script(driver)
    
    # get annotations
    target_tags = ["h1", "nav", "content", "main", "h2", "h3"]
    tag_elements_dictionary = {}    

    