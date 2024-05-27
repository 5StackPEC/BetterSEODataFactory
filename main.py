from utils import annotations, selenium, visual, web, setup
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from Lighthouse.lighthouse_utils import paralelization
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

    chunk_size = 4  # Adjust chunk size as needed
    file_path = "./Lighthouse/WebScreenshots.csv"
    try:
        print("Scraping process initiated")
        with ThreadPoolExecutor(
            max_workers=10
        ) as executor:  # Adjust number of workers as needed
            futures = []
            start_id = 0
            for chunk in paralelization.chunked_csv_reader(file_path, chunk_size):
                futures.append(
                    executor.submit(
                        paralelization.process_chunk,
                        chunk,
                        start_id,
                        driver,
                        existing_urls_in_dataset,
                    )
                )
                start_id += len(chunk)

            for future in futures:
                future.result()  # Wait for all futures to complete
        """
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
        """
    finally:
        driver.quit()
