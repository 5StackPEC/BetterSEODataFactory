from utils import web, webscraping
from Lighthouse.lighthouse_utils import reports
import json
import csv
import pandas as pd
import os
from utils import consts

# types
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Set


def generate_annotation(url, lighthouse_score, bounding_boxes_dict):
    site_name = web.get_site_name(url)
    annotation = {
        "id": site_name,
        "image": f"{site_name}.png",
        "fullURL": url,
        "score": lighthouse_score,
        "tags": bounding_boxes_dict,
    }

    return annotation


def generate_csv_annotation_header(
    header_list=consts.CSV_HEADERS,
    csv_file_path="./dataset/annotations/annotations.csv",
):
    df = pd.DataFrame(columns=header_list)
    df.to_csv(csv_file_path, index=False)
    print(f"Annotation csv file created at {csv_file_path}")


def make_annotation_on_csv_file(
    annotation_dict, csv_file_path="./dataset/annotations/annotations.csv"
):
    if not os.path.exists(csv_file_path):
        generate_csv_annotation_header(csv_file_path=csv_file_path)

    # MAKE SURE IT FOLLOWS THE PREVIOUSLY DEFINED STRUCTURE!!!!
    # [id: string, image: string, fullURL:string, score: int, tags: dictionary]
    annotation_df = pd.DataFrame([annotation_dict], columns=consts.CSV_HEADERS)

    with open(csv_file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(annotation_df.values.tolist()[0])


def generate_annotation_from_url(driver: WebDriver, url):
    driver.get(url)
    # load_js_script_to_driver(driver) # not needed atm

    # Get the bounding boxes of all the elements from the target tags
    bounding_boxes_dict = webscraping.generate_bounding_boxes_of_tags(
        driver, consts.TARGET_TAGS, url
    )

    # Process Lighthouse service
    full_lighthouse_score = reports.get_full_lighthouse_report(url)
    lighthouse_score = reports.get_seo_from_full_report(full_lighthouse_score)

    # Generate annotation dictionary
    annotation = generate_annotation(url, lighthouse_score, bounding_boxes_dict)

    return annotation


def save_failed_urls_set(
    failed_urls_set: Set[str], output_path="./dataset/annotations/failed_urls.csv"
):
    failed_urls_list = list(failed_urls_set)
    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for url in failed_urls_list:
            writer.writerow([url])


# Depracated for now
def write_json_annotation(
    annotation, json_path="./dataset/annotations/annotations.json"
):
    with open(json_path, "w") as json_file:
        json.dump(annotation, json_file)


def append_json_annotation(
    annotation, json_path="./dataset/annotations/annotations.json"
):
    with open(json_path, mode="r+") as json_file:
        json_file.seek(0, 2)
        position = json_file.tell() - 1
        json_file.seek(position)
        json_file.write(",{}]".format(json.dumps(annotation)))
