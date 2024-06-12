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
    df = pd.read_csv("data/categorised_sounds.csv")
    return df


@st.cache_data()
def load_description_data():
    csvfile = "data/clotho_captions_summarized.csv"
    df = pd.read_csv(csvfile)
    df.dropna(subset="audio_url", inplace=True)
    df = df.replace({np.nan: None})
    return df


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


def get_sounds_from_same_class():
    sounds = load_sound_data()
    available_classes = sounds["class"].unique().tolist()
    class_to_choose = random.choice(available_classes)

    samples = sounds[sounds["class"] == class_to_choose].sample(2)
    sound_1 = samples.iloc[0]
    sound_2 = samples.iloc[1]
    return (sound_1["url"], sound_1["fs_id"].item()), (sound_2["url"], sound_2["fs_id"].item())


def get_single_image():
    image_df = load_image_data()
    image = image_df.sample(1)
    return image["id"].item(), image["thumbnail"].item(), image["sound_class"].item(), image["sound_id"].item(), image["sound_url"].item()
