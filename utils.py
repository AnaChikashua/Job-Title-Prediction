import json

import pandas as pd
import data_preprocessing


def read_stop_words(file_name: str) -> list:
    stop_words = []
    with open(file_name, 'r', encoding='utf8') as words:
        for line in words:
            stop_words.append(line.rstrip())
    return stop_words


def read_csv_data(file_path: str, columns=None) -> pd.DataFrame:
    data = pd.read_csv(file_path)
    data = data.dropna(thresh=3)
    if columns:
        data = data.drop(columns, axis=1)
    return data


def read_json_data(file_path: str) -> pd.DataFrame:
    list_data = []
    with open(file_path, mode='r', errors='ignore', encoding="utf8") as json_file:
        for ob in json_file:
            list_data.append(json.loads(ob))
    return pd.DataFrame(list_data)


def save_data(data: pd.DataFrame, save_path: str):
    data.to_csv(save_path, index=False)


def load_data(csv_data_path: str, json_data_path_66: str, json_data_path_88: str):
    data = read_csv_data(csv_data_path, ["skills", "Unnamed: 0"])
    indeed_66 = read_json_data(json_data_path_66)
    indeed_88 = read_json_data(json_data_path_88)

    indeed = pd.concat([indeed_66[['job_title', 'job_description']], indeed_88[['job_title', 'job_description']]])

    indeed = indeed.rename(columns={'job_title': 'title', 'job_description': 'description'})
    data = pd.concat([data[['title', 'description']], indeed])
    return data
