import csv
import random
from dataclasses import dataclass

import numpy as np
import pandas as pd
import streamlit as st


@dataclass
class CategorisedSound:
    url: str
    ID: str
    sound_class: str


@st.cache_data()
def load_image_data():
    image_df = pd.read_csv("data/image_annotations.csv")
    return image_df


@st.cache_data()
def load_sound_data():
    with open("data/categorised_sounds.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data


@st.cache_data()
def load_description_data():
    csvfile = "data/clotho_captions_summarized.csv"
    df = pd.read_csv(csvfile)
    df.dropna(subset="audio_url", inplace=True)
    df = df.replace({np.nan: None})
    return df


def get_single_sound() -> (str, str):
    sounds = load_sound_data()
    sound = sounds[random.randint(0, len(sounds) - 1)]
    return sound["url"], sound["ID"]


def get_single_description() -> (str, str):
    descriptions = load_description_data()
    description = descriptions.sample(1).iloc[0]
    return description["filename"], description["summary_mixtral"]


def get_related_sound_for_description(source_file_name: str):
    descriptions = load_description_data()
    description = descriptions[descriptions["filename"] == source_file_name].sample(1)
    return (
        description["rel_audio_url"].item(),
        description["rel_filename"].item(),
        description["rel_start"].item(),
        description["rel_end"].item(),
    )


def get_sounds_from_same_class(sound_id: str | None = None):
    sounds = load_sound_data()
    if sound_id is None:
        available_classes = list(set([item["Class"] for item in sounds]))
        class_to_choose = random.choice(available_classes)
    else:
        class_to_choose = [item["Class"] for item in sounds if item["ID"] == sound_id][
            0
        ]

    sounds_from_same_category = [
        item for item in sounds if item["Class"] == class_to_choose
    ]

    if sound_id is None:
        random.shuffle(sounds_from_same_category)
        sound_1, sound_2 = sounds_from_same_category[:2]
    else:
        sound_1 = [
            item for item in sounds_from_same_category if item["ID"] == sound_id
        ][0]
        sounds_from_same_category.remove(sound_1)
        sound_2 = sounds_from_same_category[
            random.randint(0, len(sounds_from_same_category) - 1)
        ]
    return (sound_1["url"], sound_1["ID"]), (sound_2["url"], sound_2["ID"])


def get_sound_from_class(sd_class: str, sound_id_to_omit: str | None = None):
    sounds = load_sound_data()
    if sound_id_to_omit is None:
        sounds_from_same_category = [
            item for item in sounds if item["Class"] == sd_class
        ]
    else:
        sounds_from_same_category = [
            item
            for item in sounds
            if item["Class"] == sd_class and item["ID"] != sound_id_to_omit
        ]
    sound = sounds_from_same_category[
        random.randint(0, len(sounds_from_same_category) - 1)
    ]
    return sound["ID"], sound["url"]


def get_single_image():
    image_df = load_image_data()
    image = image_df.sample(1)
    return image["id"].item(), image["thumbnail"].item(), image["sound_class"].item(), image["sound_id"].item(), image["sound_url"].item()


if __name__ == "__main__":
    loaded_data = load_sound_data()
    print(loaded_data[0])
    print(type(loaded_data[0]["ID"]))
