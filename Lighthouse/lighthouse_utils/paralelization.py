from lighthouse_utils import reports
import csv

def process_chunk(chunk, start_id):
    for report_id, row in enumerate(chunk):
        url = row[0]
        print(url, "\n")
        try:
            report = reports.generate_report(url)
            reports.save_report(report, "lighthouse_report.json", url, start_id + report_id)
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