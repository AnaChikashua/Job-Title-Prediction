import pandas as pd
import matplotlib.pyplot as plt


def get_descriptions(data: pd.DataFrame, describe=False):
    return data.describe() if describe else data.title.value_counts(), data.title.value_counts(normalize=True)


def get_bar(data):
    fig, ax = plt.subplots()
    fig.suptitle('title_clean', fontsize=12)
    data['title_clean'].reset_index().groupby('title_clean').count().sort_values(by="index").tail(10).plot(kind="barh",
                                                                                                           legend=False,
                                                                                                           ax=ax).grid(
        axis='x')
    plt.show()
