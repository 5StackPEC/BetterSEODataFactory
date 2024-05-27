import csv
from . import reports
from utils import annotations, visual, web


def process_chunk(chunk, start_id, driver, existing_urls_in_dataset):
    for report_id, url in enumerate(chunk):
        url = url[0]
        site_name = web.get_site_name(url)
        if url in existing_urls_in_dataset:
            print(f"{site_name}: Already on dataset.")
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
        print("\n")


def process_chunk_lighthouse(chunk, start_id):
    for report_id, row in enumerate(chunk):
        url = row[0]
        print(url, "\n")
        try:
            report = reports.get_full_lighthouse_report(url)
            reports.save_report_on_file(
                report, "lighthouse_report.json", url, start_id + report_id
            )
        except Exception as e:
            print(
                "Something went wrong while generating the report"
            )  # Delete the try/except to see more details or print an "e"
            # print(e)
            continue


def chunked_csv_reader(file_path, chunk_size):
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header
        chunk = []
        for row in csvreader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:  # Yield the last chunk if it's not empty
            yield chunk
