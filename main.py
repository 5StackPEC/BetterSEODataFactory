from utils import annotations, selenium, visual, web


URLS = [
    "https://vercel.com",
    "invalidurl" "https://www.primevideo.com/",
    "https://www.netflix.com/",
    "https://www.nytimes.com/",
]

if __name__ == "__main__":
    driver = selenium.initialize_driver()
    try:
        print("Scraping process initiated")
        for url in URLS:
            print(url)
            # Generate annotation
            try:
                annotation = annotations.generate_annotation_from_url(driver, url)

                # Take screenshot
                visual.hide_scrollbar(driver)
                web.take_screenshot_of_window(driver, url)

                # Write just after everything else ran successfully
                annotations.make_annotation_on_csv_file(annotation)
            except:
                print(f"ERROR ON URL: {url}")
    finally:
        driver.quit()
