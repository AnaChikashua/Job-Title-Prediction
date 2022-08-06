import pandas as pd

import utils
import data_preprocessing
import visualization
from pathlib import Path

csv_data_path = 'media/engineering_jobs.csv'
json_data_path_66 = 'media/indeed_usa-indeed_usa_job_data__20211001_20211231_deduped_n_merged_20220305_004258919873466.ldjson'
json_data_path_88 = 'media/indeed_usa-indeed_usa_job_data__20211001_20211231_deduped_n_merged_20220305_004328202689288.ldjson'
stop_words_file_name = 'media/stop_words_english.txt'
data_path = 'media/output/result.csv'


def get_data():
    stop_words = utils.read_stop_words(stop_words_file_name)
    data = utils.load_data(csv_data_path, json_data_path_66, json_data_path_88)
    data["description_clean"] = data["description"].apply(
        lambda x: data_preprocessing.utils_preprocess_text(x, flg_stemm=False, flg_lemm=False,
                                                           lst_stopwords=stop_words))
    data["title_clean"] = data["title"].apply(
        lambda x: data_preprocessing.utils_preprocess_text(x, flg_stemm=False, flg_lemm=False,
                                                           lst_stopwords=stop_words))
    utils.save_data(data, data_path)


if __name__ == "__main__":
    print('before load data')
    path = Path(data_path)
    if not path.is_file():
        get_data()
    data = pd.read_csv(data_path)

    print("before visualization")

    print(visualization.get_descriptions(data))
