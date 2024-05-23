from utils import visual_utils
from selenium.webdriver.common.by import By

# types
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


def get_element_bounding_box(element: WebElement):
    size = element.size
    if visual_utils.is_element_size_valid(element) == False:
        return

    location = element.location
    bounding_box = [location["x"], location["y"], size["width"], size["height"]]

    return bounding_box


def get_bounding_boxes_of_tag_class(driver: WebDriver, tag_name):
    tag_elements = driver.find_elements(By.TAG_NAME, tag_name)
    elements_bounding_boxes = []
    for element in tag_elements:
        elements_bounding_boxes.append(get_element_bounding_box(element))

    return elements_bounding_boxes


def generate_bounding_boxes_of_tags(driver: WebDriver, target_tags):
    bounding_boxes_dict = {}
    for tag in target_tags:
        bounding_boxes_dict[tag] = get_bounding_boxes_of_tag_class(driver, tag)

    return bounding_boxes_dict


def load_js_script_to_driver(driver: WebDriver, js_script_path="../js/boundingBoxes.js"):
    with open(js_script_path, "r") as file:
        js_code = file.read()

    driver.execute_script(js_code)

    return driver
