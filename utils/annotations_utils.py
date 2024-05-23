from utils import web_utils
import json
import csv
import pandas as pd
import os
from utils import const


def generate_annotation(url, lighthouse_score, bounding_boxes_dict):
    site_name = web_utils.get_site_name(url)
    annotation = {
        "id": site_name,
        "image": f"{site_name}.png",
        "score": lighthouse_score,
        "tags": bounding_boxes_dict,
    }

    return annotation


def generate_csv_annotation_header(
    header_list=const.CSV_HEADERS,
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
    # [id: string, image: string, score: int, tags: dictionary]
    annotation_df = pd.DataFrame([annotation_dict], columns=const.CSV_HEADERS)

    with open(csv_file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(annotation_df.values.tolist()[0])


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
