import os
import json
from . import lighthouse


def generate_report(url):
    report = lighthouse.run_lighthouse(url)

    return report


def save_report(report, filename, url, report_id):
    if report is not None:
        important_scores = {
            "id": report_id,
            "url": url,
            "performance": report["categories"]["performance"]["score"] * 100,
            "accessibility": report["categories"]["accessibility"]["score"] * 100,
            "best-practices": report["categories"]["best-practices"]["score"] * 100,
            "seo": report["categories"]["seo"]["score"] * 100,
        }

        # Read the existing content if the file exists
        if os.path.exists(filename):
            with open(filename, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {"lighthouseReports": []}
        else:
            data = {"lighthouseReports": []}

        # Append the new report to the list
        data["lighthouseReports"].append(important_scores)

        # Write the updated data back to the file
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
            print(f"Report saved for {filename}")

        # Print scores to the console
        print("Lighthouse Performance Metrics:")
        for category, score in important_scores.items():
            if category not in ["id", "url"]:
                print(f"{category.capitalize()} score: {score}")
    else:
        print(f"No report generated for {filename}")


def thread_report(csvreader):
    for report_id, row in enumerate(csvreader):
        url = row[0]
        print(url)
        report = generate_report(url)
        # filename = f"lighthouse_report_{url.replace('https://', '').replace('/', '_')}.json"
        save_report(report, "lighthouse_report.json", url, report_id)
