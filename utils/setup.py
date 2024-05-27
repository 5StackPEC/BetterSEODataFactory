import os
import pandas as pd


def create_directories():
    required_dirs = ["./dataset", "./dataset/images", "./dataset/annotations"]

    for directory in required_dirs:
        if not os.path.exists(directory):
            print("Created output directory: ", directory)
            os.makedirs(directory)


def get_existing_website_annotations(
    default_annotations_path="./dataset/annotations/annotations.csv",
):
    try:
        df = pd.read_csv(default_annotations_path)
        return set(df["fullURL"])
    except Exception as e:
        return set()


def run_setup():
    create_directories()
