from utils import annotations_utils, selenium_utils, web_utils, visual_utils


URLS = [
    "https://vercel.com",
    "https://www.primevideo.com/",
    "https://www.netflix.com/",
    "https://www.nytimes.com/",
]

if __name__ == "__main__":
    driver = selenium_utils.initialize_driver()
    try:
        print("Scraping process initiated")
        for url in URLS:
            print(url)
            # Generate annotation
            annotation = annotations_utils.generate_annotation_from_url(driver, url)
            annotations_utils.make_annotation_on_csv_file(annotation)

            # Take screenshot
            visual_utils.hide_scrollbar(driver)
            web_utils.take_screenshot_of_window(driver, url)

    finally:
        driver.quit()
