from utils import web_utils
import json


def generate_annotation(URL, lighthouse_score, bounding_boxes_dict):
    site_name = web_utils.get_site_name(URL)
    annotation = [
        {
            f"{site_name}.png": {
                "image": site_name,
                "lightHouseScore": lighthouse_score,
                "tags": bounding_boxes_dict,
            }
        }
    ]

    return annotation


def write_json_annotation(
    annotation, json_path="./dataset/annotations/annotations.json"
):
    with open(json_path, "w") as json_file:
        json.dump(annotation, json_file)
