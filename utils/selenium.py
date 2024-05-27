from selenium import webdriver


def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    print("Driver initialized")
    return driver
