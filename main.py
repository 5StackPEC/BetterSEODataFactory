from selenium import webdriver
from utils import annotations_utils, webscraping_utils, lighthouse_utils, const

# types
from selenium.webdriver.remote.webdriver import WebDriver


def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-logging")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    print("driver initialized")
    return driver


def generate_annotation_from_url(driver: WebDriver, url):
    driver.get(url)
    # load_js_script_to_driver(driver) # not needed atm

    # Get the bounding boxes of all the elements from the target tags
    bounding_boxes_dict = webscraping_utils.generate_bounding_boxes_of_tags(
        driver, const.TARGET_TAGS
    )

    lighthouse_score = lighthouse_utils.get_lighhouse_score(url)
    annotation = annotations_utils.generate_annotation(
        url, lighthouse_score, bounding_boxes_dict
    )

    return annotation


if __name__ == "__main__":
    driver = initialize_driver()
    annotation = generate_annotation_from_url(driver, "https://vercel.com")
    annotations_utils.make_annotation_on_csv_file(annotation)
