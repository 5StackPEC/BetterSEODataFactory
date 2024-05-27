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
    failed_urls_set = set()

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
                        failed_urls_set
                    )
                )
                start_id += len(chunk)

            for future in futures:
                future.result()  # Wait for all futures to complete
    finally:
        annotations.save_failed_urls_set(failed_urls_set)
        driver.quit()
