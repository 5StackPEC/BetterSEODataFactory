from concurrent.futures import ThreadPoolExecutor
from lighthouse_utils import paralelization

if __name__ == "__main__":
    chunk_size = 10  # Adjust chunk size as needed
    file_path = "./Lighthouse/WebScreenshots.csv"

    with ThreadPoolExecutor(
        max_workers=10
    ) as executor:  # Adjust number of workers as needed
        futures = []
        start_id = 0
        for chunk in paralelization.chunked_csv_reader(file_path, chunk_size):
            futures.append(
                executor.submit(paralelization.process_chunk_lighthouse, chunk, start_id)
            )
            start_id += len(chunk)

        for future in futures:
            future.result()  # Wait for all futures to complete
