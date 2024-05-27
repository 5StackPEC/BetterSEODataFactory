from utils import annotations, selenium, visual, web, setup

URLS = [
    "https://vercel.com",
    "invalidurl",
    "https://www.primevideo.com/",
    "https://www.netflix.com/",
    "https://www.nytimes.com/",
]

if __name__ == "__main__":

    setup.run_setup()
    existing_urls_in_dataset = setup.get_existing_website_annotations()

    driver = selenium.initialize_driver()
    try:
        print("Scraping process initiated")
        for url in URLS:
            print("\n-" + url)
            if url in existing_urls_in_dataset:
                print("\tAlready on dataset.")
                continue
            # Generate annotation
            try:
                # This runs both Lighthouse and webscrapping
                annotation = annotations.generate_annotation_from_url(driver, url)

                # Take screenshot
                visual.hide_scrollbar(driver)
                web.take_screenshot_of_window(driver, url)

                # Write just after everything else ran successfully
                annotations.make_annotation_on_csv_file(annotation)
            except Exception as e:
                print(f"ERROR ON WEBSITE: {url}")
                # print(e)
    finally:
        driver.quit()
